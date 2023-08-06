#!/usr/bin/python3
from models.base_model import BaseModel

"""This is a class with a public
class attributes"""


class Place(BaseModel):
    """Place class"""

    city_id = str()  # it will be the City.id
    user_id = str()  # it will be the User.id
    name = str()
    description = str()
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = [str()]  # it will be the list of Amenity.id
