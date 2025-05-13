#!/usr/bin/env python3
"""LRU caching module that implements a basic LRU cache algorithm.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines a caching system using the LRU replacement policy.
    """

    def __init__(self):
        """Initialize the LRU cache system.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using LRU policy.

        Args:
            key: The key under which the item should be stored.
            item: The item to store.

        If the cache exceeds the maximum allowed items, it discards the
        least recently used item. If key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.order.pop(0)
            del self.cache_data[lru]
            print("DISCARD: {}".format(lru))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item by key and mark it as recently used.

        Args:
            key: The key to look up in the cache.

        Returns:
            The item if found, or None if key is None or not in cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
