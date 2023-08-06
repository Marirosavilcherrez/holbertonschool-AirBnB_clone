#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def test_type_email(self):
        obj = User()
        self.assertEqual(type(obj.email), str)

    def test_type_password(self):
        obj = User()
        self.assertEqual(type(obj.password), str)

    def test_type_firstname(self):
        obj = User()
        self.assertEqual(type(obj.first_name), str)

    def test_type_lastname(self):
        obj = User()
        self.assertEqual(type(obj.last_name), str)


if __name__ == '__main__':
    unittest.main()
