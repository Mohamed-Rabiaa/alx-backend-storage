#!/usr/bin/env python3
"""
This module contains the schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds and returns a list of all documents in a collection that contain
    a specific topic.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        topic (str): The topic to search for in the "topics" field.

    Returns:
        list: A list of documents that match the search criteria.
    """
    result = list(mongo_collection.find({"topics": {"$all": [topic]}}))
    return result
