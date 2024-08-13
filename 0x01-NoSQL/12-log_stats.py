#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

logs_count = nginx_collection.count_documents({})
print("{} logs".format(logs_count))

print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method_count = nginx_collection.count_documents({"method": method})
    print("\tmethod {}:{}".format(method, method_count))

status_check = nginx_collection.count_documents(
    {"method": "GET", "path": "/status"})
print("{} status check".format(status_check))
