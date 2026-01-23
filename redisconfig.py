from typing import AsyncIterator
from redis.asyncio import Redis, from_url
from fastapi import FastAPI
from contextlib import asynccontextmanager

REDIS_URL = "redis://localhost:6379"

@asynccontextmanager
async def lifespan(app:FastAPI) -> AsyncIterator[dict]:
    print("Startingg up redis client....")
    redis_client = from_url(REDIS_URL,decode_responses=True)
    app.state.redis = redis_client
    yield
    print('Shutting down Redis client....')
    await app.state.redis.close()

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
async def home():
    redis = app.state.redis
    await redis.set("name","Tarun")
    return({"msg":await redis.get("name")})