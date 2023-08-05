#!/usr/bin/python3

import unittest
from datetime import datetime
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_type(self):
        obj = FileStorage()
        self.assertNotEqual(obj, str)

    def test_path(self):
        obj = FileStorage.__file_path
        msg = "__file_path is None"
        self.assertIsNotNone(obj, msg)

    def test_object(self):
        obj = FileStorage.__objects
        msg = "__objects = []"
        self.assertIsInstance(obj, msg)

if __name__ == '__main__':
    unittest.main()
