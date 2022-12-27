#!/usr/bin/python3
""" Class Base"""
class Base:
    """
    Represents the "base" model for all other classes in project
    0x0C-python-almost_a_circle.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
