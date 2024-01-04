from fastapi import APIRouter, FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from game import Game
import asyncio
import json

app = FastAPI()

game_instance = Game(users=1)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

html = """
"""


@app.get("/")
# async def root():
#     return {"message": "Hello World"}
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data_json = await websocket.receive_text()
        # convert to json
        data = json.loads(data_json)
        action = data["action"]
        if action == "flip_tile":
            print("PLAYING A TILE LOL!!!")
            return_data = {"action":"flip_tile", "text": game_instance.flip_tile()}
            await websocket.send_text(json.dumps(return_data))