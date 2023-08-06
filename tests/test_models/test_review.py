#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestState(unittest.TestCase):

    def test_type_place_id(self):
        obj = Review()
        self.assertEqual(type(obj.place_id), str)

    def test_type_user_id(self):
        obj = Review()
        self.assertEqual(type(obj.user_id), str)

    def test_type_text(self):
        obj = Review()
        self.assertEqual(type(obj.text), str)

if __name__ == '__main__':
    unittest.main()
