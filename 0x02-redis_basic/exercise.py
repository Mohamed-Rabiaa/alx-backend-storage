#!/usr/bin/env python3
"""
This module provides a Cache class for storing and retrieving data using Redis.

The Cache class allows you to store data in a Redis database by generating
random keys, and it provides basic functionality for managing the cache.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for interacting with a Redis database.

    This class provides methods to store data in Redis with a randomly
    generated key and retrieve it when needed. It initializes a Redis
    client instance upon creation and flushes the database to ensure
    a clean slate.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance.

        This constructor creates a Redis client instance and stores it as
        a private variable named _redis. It also flushes the Redis database
        to clear any existing data, ensuring that the cache starts with
        a fresh state.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis database with a randomly generated key.

        This method generates a unique random key using the uuid module,
        stores the provided data in Redis using this key, and returns
        the key to the caller. The data can be of any type that Redis supports.

        Args:
            data: The data to be stored in the Redis cache.

        Returns:
            str: The randomly generated key associated with the stored data.
        """
        self.key = str(uuid.uuid4())
        self._redis.set(self.key, data)
        return self.key
