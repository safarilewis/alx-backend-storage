#!/usr/bin/env python3
'''Python file that perfoms basic operations using redis'''
import redis
import uuid
from typing import Callable, Union, Any


class Cache:
    '''Class that represents a storage container'''

    def __init__(self) -> None:
        '''Initializes redis with set params'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores items in redis'''
        data_id = str(uuid.uuid4())
        self._redis.set(data_id, data)
        return data_id

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        '''Get method that converts redis strings to UTF-8'''
        elem = self._redis.get(key)
        if fn is not None:
            return fn(elem)
        else:
            return elem

        def get_str(self, key: str) -> str:
            '''Gets a string value from redis'''
            return self.get(key, lambda x: x.decode('utf-8'))

        def get_int(self, key) -> str:
            '''Gets an int value from redis'''
            return self.get(key, lambda x: int(x))
