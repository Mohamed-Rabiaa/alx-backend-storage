#!/usr/bin/env python3
"""
This module contains the top_students function
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection (Collection): The pymongo collection object.

    Returns:
        list[Dict]: a list of all students sorted by average score
    """
    return list(mongo_collection.aggregate([
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]))
