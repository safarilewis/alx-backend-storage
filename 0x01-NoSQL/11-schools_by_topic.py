#!/usr/bin/env python3
'''task 11'''


def schools_by_topic(mongo_collection, topic):
    '''Queries schools based on topics'''
    myquery = {"topics": topic}
    mongo_collection.find_many(myquery)
