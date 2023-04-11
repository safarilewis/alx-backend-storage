#!/usr/bin/env python3
'''Listing docs in mongodb using pymongo'''
from pymongo import MongoClient
import pprint


def list_all(mongo_collection):
    """Returns collection"""
    if mongo_collection.find() == NULL:
        return []
    for doc in mongo_collection.find():
        return doc
