#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestState(unittest.TestCase):

    def test_type_city_id(self):
        obj = Place()
        self.assertEqual(type(obj.city_id), str)

    def test_type_user_id(self):
        obj = Place()
        self.assertEqual(type(obj.user_id), str)

    def test_type_name(self):
        obj = Place()
        self.assertEqual(type(obj.name), str)

    def test_type_description(self):
        obj = Place()
        self.assertEqual(type(obj.description), str)

    def test_type_number_rooms(self):
        obj = Place()
        self.assertEqual(type(obj.number_rooms), int)

    def test_type_number_bathrooms(self):
        obj = Place()
        self.assertEqual(type(obj.number_bathrooms), int)

    def test_type_max_guest(self):
        obj = Place()
        self.assertEqual(type(obj.max_guest), int)

    def test_type_price_by_night(self):
        obj = Place()
        self.assertEqual(type(obj.price_by_night), int)

    def test_type_latitude(self):
        obj = Place()
        self.assertEqual(type(obj.latitude), float)

    def test_type_longitude(self):
        obj = Place()
        self.assertEqual(type(obj.longitude), float)

    def test_type_amenity_ids(self):
        obj = Place()
        self.assertEqual(type(obj.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
