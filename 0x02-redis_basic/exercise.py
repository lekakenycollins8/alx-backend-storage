#!/usr/bin/env python
"""Create a Cache class. In the __init__ method, store an instance of the Redis
client as a private variable named _redis (using redis.Redis()) and flush the
instance using flushdb.
Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.Type-annotate
store correctly. Remember that data can be a
str, bytes, int or float.
create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.
Remember to conserve the original Redis.get behavior if the key does not exist.
Also, implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.
In this task, we will implement a system to count how many times methods of the Cache class are called.

Above Cache define a count_calls decorator that takes a single method Callable argument and returns a Callable.

As a key, use the qualified name of method using the __qualname__ dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.
"""


import redis
import uuid
from typing import Union, Optional, Callable

def count_calls(method: Callable) -> Callable:
    """count calls decorator"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """creates a cache class with redis instance"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates and returns random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get data from redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """get data from redis and return as string"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """get data from redis and return as int"""
        data = self._redis.get(key)
        try:
            data = int(data.decode('utf-8'))
        except Exception:
            data = 0
        return data