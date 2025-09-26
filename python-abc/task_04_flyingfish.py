#!/usr/bin/env python3
"""FlyingFish multiple inheritance example."""

class Fish:
    """Fish class."""
    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat for fish."""
        print("The fish lives in water")


class Bird:
    """Bird class."""
    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat for bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from Fish and Bird."""

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    print(FlyingFish.mro())  # or FlyingFish.__mro__
