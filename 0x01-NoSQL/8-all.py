#!/usr/bin/env python3
'''Listing docs in mongodb using pymongo'''
from pymongo import MongoClient


def list_all(mongo_collection):
    """Returns collection"""
    for doc in mongo_collection.find():
        return [doc]
