#!/usr/bin/env python3
"""Module defining CountedIterator that tracks iteration count."""

class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        return self.count
