#!/usr/bin/env python3
'''Nginx logs'''
from pymongo import MongoClient


def nginx_logs_collection(nginx_collection):
    '''Returns information about nginx logs collection'''
    print("{} logs".format(nginx_collection.count_documents({})))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method,
                                       nginx_collection.count_documents({"method": method})))
    print("{} status check".format(nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})))


def start():
    '''starts connection to mongodb'''
    client = MongoClient(host="localhost", port=27017)
    nginx_logs_collection(client.logs.nginx)


if __name__ == '__main__':
    start()
