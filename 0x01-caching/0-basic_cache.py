#!/usr/bin/env python3
""" BaseCaching module implimentation
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache system
    """
    def __init__(self):
        """
        Initialize the init method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Cache a key-value
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return none
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
