from time import time_ns

import uvicorn
from decouple import config
from fastapi import FastAPI

from redis_client import redis_client

app = FastAPI()

def generate_token():
    return str(time_ns())

@app.post("/authorize/")
def authorize(user_id: int):
    token = generate_token()
    status = redis_client.set(token, str(user_id), ex=60 * 60)
    return {
        'success': status,
        'token': token
    }

@app.get("/getByToken/")
def getByToken(token: str):
    user = redis_client.get(token)
    return {
        'userId': user
    }


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(config('SERVICE_PORT')))
