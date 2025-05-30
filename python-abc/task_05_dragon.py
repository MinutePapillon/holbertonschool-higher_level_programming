#!/usr/bin/env python3
"""Module defining mixins and a Dragon class demonstrating multiple behaviors."""


class SwimMixin:
    """Mixin that provides swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar."""

    def roar(self):
        print("The dragon roars!")
