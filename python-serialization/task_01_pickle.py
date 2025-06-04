#!/usr/bin/python3
"""Module for serializing and deserializing a custom object using pickle."""
import pickle


class CustomObject:
    """Class representing a custom object with basic attributes."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object to the given filename."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Optionnel : log ou raise selon les besoins

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an object from the given filename."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
