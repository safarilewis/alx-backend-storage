#!/usr/bin/env python3
'''Listing docs in mongodb using pymongo'''
from pymongo import MongoClient


def list_all(mongo_collection):
    """Returns collection"""
    if not mongo_collection.find():
        return []
    return [doc for doc in mongo_collection.find()]
       
