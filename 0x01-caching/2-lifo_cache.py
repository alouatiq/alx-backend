#!/usr/bin/env python3
"""LIFO caching module that implements a basic LIFO cache algorithm.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system using the LIFO replacement policy.
    """

    def __init__(self):
        """Initialize the LIFO cache system.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using LIFO policy.

        Args:
            key: The key under which the item should be stored.
            item: The item to store.

        If the cache exceeds the maximum allowed items, it discards the
        last inserted item (LIFO). If key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.order.pop()
            del self.cache_data[discarded]
            print("DISCARD: {}".format(discarded))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item by key.

        Args:
            key: The key to look up in the cache.

        Returns:
            The item if found, or None if key is None or not in cache.
        """
        return self.cache_data.get(key, None)
