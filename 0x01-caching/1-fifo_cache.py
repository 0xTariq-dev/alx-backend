#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache Defines: First-in First-out Cashing System
      - This caching system have limit of four items
      - If the limit is reached the first item in the cache is
        replaced with the new item
    """
    def __init__(self):
        """ Initiliaze Method """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) == self.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                self.cache_data.pop(first)
                print(f'DISCARD: {first}')
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
