#!/usr/bin/python3
"""Defines class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an exception for unimplemented area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
