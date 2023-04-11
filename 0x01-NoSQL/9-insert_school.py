#!/usr/bin/env python3
"""Script to insert documents in mongo collection"""


def insert_school(mongo_collection, **kwargs):
    """Loops through kwargs and adds them to collection"""
    for key, value in kwargs:
        school = [key, value]
    mongo_collection.insert_one(school)