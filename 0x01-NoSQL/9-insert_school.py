#!/usr/bin/env python3
"""
This module contains the insert_school function
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
      mongo_collection (Collection): The pymongo collection object.
      kwargs: The fields and values for the document to be inserted
      into the collection.

    Returns:
      ObjectId: The _id of the inserted document.
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
