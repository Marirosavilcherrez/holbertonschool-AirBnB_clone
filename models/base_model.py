#!/usr/bin/python3
import uuid
import datetime
"""This is a class BaseModel that defines all common
attributes/methods for other classes"""


class BaseModel:
    "BaseModel class"

    def __init__(self):
        "This is a constructor"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """This function print the class, id and dict
        and return them"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Function to update the public instance attribute"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """Public instance return a dictionary containig all keys/value
        and return it with __class__"""
        full_dict = self.__dict__.copy()
        full_dict["created_at"] = self.created_at.isoformat()
        full_dict["updated_at"] = self.updated_at.isoformat()
        full_dict["__class__"] = self.__class__.__name__
        return full_dict
