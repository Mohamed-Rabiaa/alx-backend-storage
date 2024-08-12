#!/usr/bin/env python3
"""
This module contains the list_all function
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
      mongo_collection (Collection): The pymongo collection object

    Returns:
      List[Dict]: a list of all documents in a collection.
    """
    result = list(mongo_collection.find())
    if not result:
        result = []
    return result
