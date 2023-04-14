#!/usr/bin/env python3
'''A module that implements an expiring web cache and tracker'''
import requests
import redis
from functools import wraps
from typing import Callable
client = redis.Redis()


def data_cache(method: Callable) -> Callable:
    '''Caches data from the url'''
    @wraps(method)
    def invoke(url: str):
        '''Wrapper function'''
        client.incr(f'count:{url}')
        result = client.get(f'result:{url}')
        return result.decode('utf-8')
        result = method(url)
        client.set(f'count:{url}', 0)
        client.setex(f'result:{url}', 10, result)
        return result
    return invoke


@data_cache
def get_page(url: str) -> str:
    '''Core function that implements the caching'''
    return requests.get(url).text
