#!/usr/bin/env python3
"""task 10"""


def update_topics(mongo_collection, name, topics):
    '''Updates topics based on the name given'''
    newValues = {"$set": {topics}}
    mongo_collection.update_one(name, newValues)
