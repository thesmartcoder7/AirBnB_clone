#!/usr/bin/python3
"""
Module for the FileStorage class.

This module defines the FileStorage class, which is responsible for serializing
instances to a JSON file and deserializing JSON file to instances.

"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.

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
        """
        Deserializes the JSON file to __objects.

        """
        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    module = __import__(
                        'models.' 'base_model', fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj_instance = class_(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
