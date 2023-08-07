#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def initial_test(self):
        object = BaseModel()
        self.assertIsInstance(object.id, str)

    def test_str_method(self):
        object = BaseModel()
        expected_str = '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                             self.__dict__)
        self.assertNotEqual(str(object), expected_str)

    def test_time_now(self):
        object = BaseModel()
        expected_time = datetime.now()
        self.assertEqual(object.created_at, expected_time)

    def test_time_created(self):
        object = BaseModel()
        self.assertEqual(object.created_at, object.updated_at)

    def test_dict(self):
        object = BaseModel()
        full_dict = object.to_dict()
        self.assertNotEqual(full_dict, self.__dict__)


if __name__ == '__main__':
    unittest.main()
