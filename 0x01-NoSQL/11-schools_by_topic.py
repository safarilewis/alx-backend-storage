#!/usr/bin/env python3
'''task 11'''


def schools_by_topic(mongo_collection, topic):
    '''Returns schools based on topics'''
    return [mongo_collection.find_many({"topics": topic})]
