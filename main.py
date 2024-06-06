import random
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def pong() -> dict:
    return {"data": "pong!"}

@app.post('/ai-move')
def ai_move(data: dict) -> int:
    '''
    @body: input [int, int, int, int] -> use it directly to model
    @return: It will return the direction in which the AI should move.
    '''
    # NOTE: [int, int, int, int]의 형태, model input에 사용
    board_info = data["board"].split(' ')
    
    # TODO: board_info를 가지고 모델을 통해 예측한 방향을 리턴해야함. 0: 좌, 1: 상, 2: 우, 3: 하
    res = random.randint(0, 3)
    return res