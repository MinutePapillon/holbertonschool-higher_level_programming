#!/usr/bin/env python3
"""
Shapes with an abstract base class and a duck-typed consumer.
"""

from abc import ABC, abstractmethod
import math
from typing import Any

class Shape(ABC):
    """Abstract base class that defines the shape interface."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Area = π * r^2"""
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """Perimeter (circumference) = 2 * π * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Area = width * height"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Perimeter = 2 * (width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape: Shape) -> None:
    """
    Print the area and perimeter of `shape`.

    This function uses duck typing: it does not check the object's type,
    it simply calls .area() and .perimeter() and expects them to exist.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Quick local test (this block does not run when module is imported)
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
