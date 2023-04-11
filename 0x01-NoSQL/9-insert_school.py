#!/usr/bin/env python3
"""Script to insert documents in mongo collection"""


def insert_school(mongo_collection, **kwargs):
    """Loops through kwargs and adds them to collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
