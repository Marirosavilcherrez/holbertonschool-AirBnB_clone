#!/usr/bin/python3
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""This is a class FileStorage that serializes instance
to a JSON file and desealizes in JSON format"""


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serealizes"""
        dic_store = {}
        for key, value in FileStorage.__objects.items():
            dic_store[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8")\
                as document:
            document.write(json.dumps(dic_store))

    def reload(self):
        """Deserealizes"""
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as doc:
                data_file = doc.read()
                store_json = json.loads(data_file)
                for key, value in store_json.items():
                    value = store_json[key]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = obj
        else:
            pass
