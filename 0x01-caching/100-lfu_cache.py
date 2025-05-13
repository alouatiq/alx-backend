#!/usr/bin/env python3
"""LFU caching module that implements LFU with LRU tie-break policy.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a caching system using the LFU replacement policy.
    """

    def __init__(self):
        """Initialize the LFU cache system.
        """
        super().__init__()
        self.freq = {}
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using LFU policy.

        Args:
            key: The key under which the item should be stored.
            item: The item to store.

        If the cache exceeds the maximum allowed items, it discards the
        least frequently used item. If there's a tie, discard the LRU one.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq[key] += 1
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                candidates = [
                    k for k in self.order if self.freq[k] == min_freq
                ]
                discard = candidates[0]
                del self.cache_data[discard]
                del self.freq[discard]
                self.order.remove(discard)
                print("DISCARD: {}".format(discard))
            self.freq[key] = 1

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item by key and update its frequency.

        Args:
            key: The key to look up in the cache.

        Returns:
            The item if found, or None if key is None or not in cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
