#!/usr/bin/env python3
"""
This module provides a Cache class for storing and retrieving data using Redis.

The Cache class allows you to store data in a Redis database by generating
random keys, and it provides basic functionality for managing the cache.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count_calls decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper


def replay(method):
    """
    Display the history of calls of a particular function.

    Args:
        method: the function to display its history of calls
    """
    r = redis.Redis()
    name = method.__qualname__
    calls_count = int(r.get(name))
    print("{} was called {} times:".format(name, calls_count))

    inputs = r.lrange("{}:inputs".format(name), 0, -1)
    outputs = r.lrange("{}:outputs".format(name), 0, -1)
    combo_lst = list(zip(inputs, outputs))
    for (i, o) in combo_lst:
        print("{}(*{}) -> {}".format(name, i.decode("utf-8"),
                                     o.decode("utf-8")))


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

    @count_calls
    @call_history
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

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieve data from the Redis database by key.

        This method retrieves data from Redis using the provided key.
        If a callable `fn` is provided, it will be used to convert the data
        back to the desired format. If the key does not exist,
        None is returned.

        Args:
            key: The key to retrieve from the Redis cache.
            fn: A callable used to convert the data back to the desired format.

        Returns:
            The data associated with the key, potentially converted using `fn`,
            or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from the Redis database by key.

        This method retrieves data from Redis using the provided key and
        decodes it as a UTF-8 string.

        Args:
            key: The key to retrieve from the Redis cache.

        Returns:
            str: The string associated with the key, or None if the key
            does not exist.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from the Redis database by key.

        This method retrieves data from Redis using the provided key and
        converts it to an integer.

        Args:
            key: The key to retrieve from the Redis cache.

        Returns:
            int: The integer associated with the key, or None if the key
            does not exist.
        """
        return self.get(key, int)
