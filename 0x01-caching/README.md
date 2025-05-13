# 0x01. Caching

## Description

This project covers the implementation of various caching algorithms in
Python. Each class defines a specific cache replacement policy using a
common base class `BaseCaching`. The purpose is to learn how different
caching mechanisms work and to implement them according to standard
specifications.

## Technologies

- Python 3.7
- Ubuntu 18.04 LTS
- `pycodestyle` (PEP8) compliance
- Executable script files

## Files

| Filename            | Description                                |
|---------------------|--------------------------------------------|
| `0-basic_cache.py`  | Implements a basic cache with no eviction  |
| `1-fifo_cache.py`   | Implements FIFO (First-In, First-Out)      |
| `2-lifo_cache.py`   | Implements LIFO (Last-In, First-Out)       |
| `3-lru_cache.py`    | Implements LRU (Least Recently Used)       |
| `4-mru_cache.py`    | Implements MRU (Most Recently Used)        |
| `100-lfu_cache.py`  | Implements LFU (Least Frequently Used)     |
| `base_caching.py`   | Defines the base class `BaseCaching`       |

## Learning Objectives

- Understand what a caching system is
- Learn different cache eviction policies:
  - FIFO
  - LIFO
  - LRU
  - MRU
  - LFU
- Understand the limitations and use cases for each method

## Usage

Each script can be tested using its corresponding `*-main.py` file provided
in the project. These demonstrate how the caching class behaves.

```bash
./0-main.py
./1-main.py
...
```
