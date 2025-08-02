from fastapi import FastAPI
from contextlib import asynccontextmanager
from websocket.broker import RabbitMQBroker

from .api import user_routes
from websocket.routers import router as websocket_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  

app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router)
app.include_router(websocket_router)

