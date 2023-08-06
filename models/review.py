#!/usr/bin/python3
from models.base_model import BaseModel

"""This is a class with a public
class attributes"""


class Review(BaseModel):
    """Review class"""

    place_id = str()  # it will be the Place.id
    user_id = str()  # it will be the User.id
    text = str()
