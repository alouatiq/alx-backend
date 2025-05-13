#!/usr/bin/env python3
"""FIFO caching module that implements a basic FIFO cache algorithm.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system using the FIFO replacement policy.
    """

    def __init__(self):
        """Initialize the FIFO cache system.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO policy.

        Args:
            key: The key under which the item should be stored.
            item: The item to store.

        If the cache exceeds the maximum allowed items, it discards the
        first inserted item (FIFO). If key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
            self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key.

        Args:
            key: The key to look up in the cache.

        Returns:
            The item if found, or None if key is None or not in cache.
        """
        return self.cache_data.get(key, None)
