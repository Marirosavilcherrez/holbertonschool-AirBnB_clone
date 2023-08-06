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
        obj = FileStorage()
        obj.__file_path = "file"
        self.assertEqual(obj.__file_path, "file")

    def test_object(self):
        objec = FileStorage()
        objec.__objects = {}
        self.assertEqual(objec.__objects, {})

if __name__ == '__main__':
    unittest.main()
