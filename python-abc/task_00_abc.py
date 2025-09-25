#!/usr/bin/python3
"""
Abstract Animal example with Dog and Cat subclasses.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """
    @abstractmethod
    def sound(self):
        """
        Return the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class, inherits from Animal.
    """
    def sound(self):
        """
        Return dog sound.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class, inherits from Animal.
    """
    def sound(self):
        """
        Return cat sound.
        """
        return "Meow"
