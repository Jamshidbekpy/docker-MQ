from fastapi import FastAPI

from .api import user_routes
from websocket.router import router as websocket_router

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(websocket_router)

