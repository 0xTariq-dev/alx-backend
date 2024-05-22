#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCashe Defines: Basic Cashing System
      - This caching system doesn't have limit
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze Method """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
