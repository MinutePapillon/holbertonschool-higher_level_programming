#!/usr/bin/env python3
"""CountedIterator class that counts iterations."""

class CountedIterator:
    """Iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize with an iterable and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
