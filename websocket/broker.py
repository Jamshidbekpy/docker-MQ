import uuid
from aio_pika import connect_robust, Message, IncomingMessage, DeliveryMode
from typing import Callable

class RabbitMQBroker:
    def __init__(self, url="amqp://guest:guest@localhost/"):
        self.url = url
        self.exchange_name = "chat_direct"
        self.routing_key = "chat"
        self.queue_name = "chat_queue" 

    async def connect(self, on_message: Callable[[str], None]):
        self.connection = await connect_robust(self.url)
        self.channel = await self.connection.channel()

        self.exchange = await self.channel.declare_exchange(
            self.exchange_name,
            type="direct",
            durable=True
        )

        self.queue = await self.channel.declare_queue(
            name=self.queue_name,
            durable=True,
            exclusive=False,
            auto_delete=False
        )

        await self.queue.bind(self.exchange, routing_key=self.routing_key)

        async def handle(msg: IncomingMessage):
            async with msg.process():
                text = msg.body.decode()
                await on_message(text)

        await self.queue.consume(handle)

    async def publish(self, message: str):
        await self.exchange.publish(
            Message(
                message.encode(),
                delivery_mode=DeliveryMode.PERSISTENT  
            ),
            routing_key=self.routing_key
        )

    async def remove_queue(self):
        await self.queue.delete()
