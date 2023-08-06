#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestState(unittest.TestCase):

    def test_type_placeid(self):
        obj = Amenity()
        self.assertEqual(type(obj.name), str)


if __name__ == '__main__':
    unittest.main()
