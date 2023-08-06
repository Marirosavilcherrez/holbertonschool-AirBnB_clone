#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""This is a class BaseModel that defines all common
attributes/methods for other classes"""


class BaseModel:
    "BaseModel class"

    def __init__(self, *args, **kwargs):
        "This is a constructor"
        if kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """This function print the class, id and dict
        and return them"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Function to update the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Public instance return a dictionary containig all keys/value
        and return it with __class__"""
        full_dict = dict(self.__dict__)
        full_dict["created_at"] = self.created_at.isoformat()
        full_dict["updated_at"] = self.updated_at.isoformat()
        full_dict["__class__"] = self.__class__.__name__
        return full_dict
