from fastapi import WebSocket
from ..manager import ConnectionManager
from .interfaces import AbstractWebSocketService
from ..broker import RabbitMQBroker

class WebSocketService(AbstractWebSocketService):
    def __init__(self, manager: ConnectionManager, broker: RabbitMQBroker):
        self.manager = manager
        self.broker = broker

    async def handle_connection(self, websocket: WebSocket):
        await self.manager.connect(websocket)
        try:
            while True:
                message = await websocket.receive_text()
                await self.broker.publish(message)
        except Exception as e:
            print("Disconnected {e}")
            self.manager.disconnect(websocket)
