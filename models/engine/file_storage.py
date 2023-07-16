#!/usr/bin/python3
"""
Module for the FileStorage class.

This module defines the FileStorage class, which is responsible for
serializing instances to a JSON file and deserializing JSON file to
instances.

"""

import json
from os.path import exists


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances.

    Private class attributes:
    - __file_path: string - path to the JSON file (ex: file.json)
    - __objects: dictionary - stores all objects by <class name>.id

    Public instance methods:
    - all(self): Returns the dictionary __objects.
    - new(self, obj): Sets in __objects the obj with key <obj class name>.id.
    - save(self): Serializes __objects to the JSON file.
    - reload(self): Deserializes the JSON file to __objects.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: A dictionary containing all objects by <class name>.id.

        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: An instance of a class.

        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.

        """
        serialized_objects = {
            key: value.to_dict() for key, value in self.__objects.items()
        }
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                decereal = json.load(jsonfile)
            for keys in decereal.keys():
                if decereal[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**decereal[keys])
                elif decereal[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**decereal[keys])
                elif decereal[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**decereal[keys])
                elif decereal[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**decereal[keys])
                elif decereal[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**decereal[keys])
                elif decereal[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**decereal[keys])
                elif decereal[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**decereal[keys])
                else:
                    ...
