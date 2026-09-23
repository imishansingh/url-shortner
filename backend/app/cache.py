import os

import redis
from fastapi import Depends, HTTPException, status

from .auth import get_current_user
from .models import User

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True,
)

RATE_LIMIT = 5
WINDOW_SECONDS = 60


def check_rate_limit(current_user: User = Depends(get_current_user)):
    key = f"ratelimit:{current_user.id}"
    count = redis_client.incr(key)
    if count == 1:
        redis_client.expire(key, WINDOW_SECONDS)
    if count > RATE_LIMIT:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded, try again later")
