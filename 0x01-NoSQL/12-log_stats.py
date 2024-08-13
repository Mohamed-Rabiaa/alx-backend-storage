#!/usr/bin/env python3
"""
This script contains the nginx_log_states function
"""

from pymongo import MongoClient


def nginx_log_states(nginx_collection):
    """
    provides some stats about Nginx logs stored in MongoDB

    Args:
      nginx_collection (Collection): The nginx collection
    """
    logs_count = nginx_collection.count_documents({})
    print("{} logs".format(logs_count))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    nginx_log_states(nginx_collection)
