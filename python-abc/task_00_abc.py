#!/usr/bin/env python3
"""Module defining an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        return "Meow"
