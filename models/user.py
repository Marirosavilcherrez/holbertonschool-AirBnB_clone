#!/usr/bin/python3
from models.base_model import BaseModel

"""This is a class with a public
class attributes"""


class User(BaseModel):
    """User class"""

    def __init__(self):
        """This is a constructor"""
        self.email = str()
        self.password = str()
        self.first_name = str()
        self.last_name = str()
