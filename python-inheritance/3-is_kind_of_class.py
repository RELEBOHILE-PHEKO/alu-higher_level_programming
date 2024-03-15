#!/usr/bin/python3

"""
Module is_kind_of_class

Provides a function to check if an object is an instance of a given class or any of its subclasses.
"""

def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of a class or a subclass of that class.

    Args:
        obj: Any object to be evaluated.
        a_class: A class or type to check against.

    Returns:
        bool: True if the object is an instance of the given class or any of its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
