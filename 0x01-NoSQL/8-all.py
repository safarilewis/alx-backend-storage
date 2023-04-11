#!/usr/bin/env python3
from pymongo import MongoClient
import pprint

def list_all(mongo_collection):
    if mongo_collection.find() == NULL:
        return []
    for doc in mongo_collection.find():
        pprint.pprint(doc)
