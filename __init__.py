#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
A mongo package for use easily

author lipuyeh
"""

import mongo_tools.setting as mongo_setting

from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_client = None

def get_mongo(mongo_ip=None, mongo_port=27017):

    if mongo_ip == None:
        mongo_ip = mongo_setting.server_ip
        mongo_port = mongo_setting.port
    else:
        pass

    mongo_url = 'mongodb://%s:%s/' % (mongo_ip, mongo_port)
    client = MongoClient(mongo_url)

    return client


def find(db_name, col_name, cond):

    global mongo_client
    if mongo_client is None:
        mongo_client = get_mongo()
    else:
        pass

    cursor = mongo_client[db_name][col_name].find(cond)
    results = []
    for a_data in cursor:
        results.append(a_data)

    return results



def insert(db_name, col_name, doc):

    global mongo_client
    if mongo_client is None:
        mongo_client = get_mongo()
    else:
        pass

    inserted_id = mongo_client[db_name][col_name].insert_one(doc).inserted_id

    return inserted_id

if __name__ == '__main__':

    # Test
    pass
