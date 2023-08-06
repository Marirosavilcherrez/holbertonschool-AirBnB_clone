#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestState(unittest.TestCase):

    def test_type(self):
        obj = City()
        self.assertEqual(type(obj.name), str)


if __name__ == '__main__':
    unittest.main()
