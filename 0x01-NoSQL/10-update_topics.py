#!/usr/bin/env python3
"""
This module contains the update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of all documents in a collection with a specific name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the documents to update.
        topics (list): The list of topics to set for the documents.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
