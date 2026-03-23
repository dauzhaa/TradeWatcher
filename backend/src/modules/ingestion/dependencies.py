import redis.asyncio as redis
from src.core.config import settings
from contextlib import asynccontextmanager

pool = redis.ConnectionPool.from_url(settings.REDIS_URL)

@asynccontextmanager
async def get_redis_client():
    client = redis.Redis.from_pool(pool)
    try:
        yield client
    finally:
        await client.aclose()

