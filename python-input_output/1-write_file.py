#!/usr/bin/python3
"""Module for writing text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return char count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
