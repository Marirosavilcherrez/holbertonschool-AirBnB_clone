#!/usr/bin/python3
from models.base_model import BaseModel

"""This is a class State with a public
class attributes"""


class City(BaseModel):
    """City class"""

    state_id = str()  # it will be the state.id
    name = str()
