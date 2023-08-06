#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

class TestFileStorage(unittest.TestCase):

    def test_path(self):
        obj = FileStorage()
        setattr(obj, '_FileStorage__file_path', "file")
        self.assertEqual(obj._FileStorage__file_path, "file")

    def test_object(self):
        objec = FileStorage()
        setattr(objec, '_FileStorage__objects', {})
        self.assertEqual(objec._FileStorage__objects, {})


if __name__ == '__main__':
    unittest.main()
