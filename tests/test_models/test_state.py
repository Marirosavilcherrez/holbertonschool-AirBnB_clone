#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_type(self):
        obj = State()
        self.assertEqual(type(obj.name), str)


if __name__ == '__main__':
    unittest.main()
