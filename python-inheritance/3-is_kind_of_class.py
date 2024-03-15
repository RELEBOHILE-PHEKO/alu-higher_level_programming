#!/usr/bin/python3
"""Module is_kind_of_class
Finds if the object is an instance of, or if object is an
instance of a class that inherited from, the specified class
"""

def is_kind_of_class(obj, a_class):
    """
    Determines if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj: Any object to be evaluated.
        a_class: A class or type to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
