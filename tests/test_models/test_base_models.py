#!/usr/bin/python3

"""
test_base_model.py

This module contains unit tests for the BaseModel class.

"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    """
    Unit tests for the BaseModel class.

    """

    def setUp(self):
        """
        Set up the necessary objects for each test method.

        """
        self.model = BaseModel()

    def test_id_is_string(self):
        """
        Test that the id attribute of BaseModel is a string.

        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test that the created_at attribute of BaseModel
        is an instance of datetime.

        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test that the updated_at attribute of BaseModel
        is an instance of datetime.

        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test that the save() method updates the updated_at attribute.

        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_contains_class_name(self):
        """
        Test that the to_dict() method contains the class name
        in the returned dictionary.

        """
        obj_dict = self.model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        """
        Test that the to_dict() method contains the created_at attribute
        in the returned dictionary.

        """
        obj_dict = self.model.to_dict()
        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['created_at'],
                         self.model.created_at.isoformat())

    def test_to_dict_contains_updated_at(self):
        """
        Test that the to_dict() method contains the updated_at attribute
        in the returned dictionary.

        """
        obj_dict = self.model.to_dict()
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str_representation(self):
        """
        Test the string representation of the BaseModel instance.

        """
        model_str = str(self.model)
        self.assertIn('BaseModel', model_str)
        self.assertIn(self.model.id, model_str)
        self.assertIn(str(self.model.__dict__), model_str)

    def test_init_recreates_instance_from_dict(self):
        """
        Test that the __init__ method can recreate an instance from
        a dictionary representation.

        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_init_recreates_instance_with_new_id_and_created_at(self):
        """
        Test that the __init__ method creates a new instance with a new id
        and created_at if not provided in the dictionary representation.

        """
        model_dict = self.model.to_dict()
        model_dict.pop('id')
        model_dict.pop('created_at')

        new_model = BaseModel(**model_dict)

        self.assertNotEqual(new_model.id, self.model.id)
        self.assertIsInstance(new_model.id, str)


if __name__ == '__main__':
    unittest.main()
