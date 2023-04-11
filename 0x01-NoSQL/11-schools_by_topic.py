#!/usr/bin/env python3
'''task 11'''


def schools_by_topic(mongo_collection, topic):
    '''Queries schools based on topics'''
    myquery = {"topics": {"$eq": topic}}
    return [doc for doc in mongo_collection.find(myquery)]
