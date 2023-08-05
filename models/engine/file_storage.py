#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
"""This is a class FileStorage that serializes instance
to a JSON file and desealizes in JSON format"""


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__name__, obj.id)] = obj

    def save(self):
        """Serealizes"""
        with open(self.__file_path, mode="w", encoding="UTF-8") as document:
            dic_storage = {}
            for key, value in self.__objects.items():
                dic_storage[key] = value.to_dic()
            document.write(json.dumps(dic_storage))

    def reload(self):
        """Deserealizes"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as document:
                read_doc = document.read()
                dict_storage = json.loads(read_doc)
                for key, value in dict_storage.items():
                    value = dic_storage.items()
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        else:
            pass
