#!/usr/bin/env python3
'''Python file that perfoms basic operations using redis'''
import redis
import uuid


class Cache:
    '''Class that represents a storage container'''

    def __init__(self) -> None:
        '''Initializes redis with set params'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores item in redis'''
        data_id = str(uuid.uuid4())
        self._redis.set(data_id, data)
        return data_id
    
