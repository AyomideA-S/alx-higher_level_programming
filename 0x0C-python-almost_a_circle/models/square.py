#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defining the class Rectangle that innherits from class Base """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """module string represation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
