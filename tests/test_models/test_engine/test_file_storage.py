#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

class TestFileStorage(unittest.TestCases):

    def test_file_path(self):
        file_path = fileStorage.__file_path
        self.assertIsNotNone(file_path, '__file_path is none')


if __name__ == '__main__':
    unittest.main()
