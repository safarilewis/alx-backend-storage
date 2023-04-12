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
        self._redis.set(data, data_id)
        return data_id
