#!/usr/bin/python3
""" Rectangle Base"""
from models.base import Base


class Rectangle(Base):
    ''' Defining the class Rectangle that innherits from class Base '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
