#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defining the class Rectangle that innherits from class Base """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String represation of square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """ Square size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Square size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates arguments in Square """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictonary representation of class Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
