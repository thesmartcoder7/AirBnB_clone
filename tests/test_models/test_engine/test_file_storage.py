#!/usr/bin/python3

"""
Module containing unit tests for the FileStorage class.

"""

import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTestCase(unittest.TestCase):
    """
    Unit tests for the FileStorage class.

    """

    def setUp(self):
        """
        Set up the necessary objects for each test method.

        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after each test method.

        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_empty(self):
        """
        Test that the all() method returns an empty dictionary when there are no objects in storage.

        """
        objects = self.storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        """
        Test that the new() method adds a new object to storage.

        """
        model = BaseModel()
        self.storage.new(model)
        objects = self.storage.all()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, objects)
        self.assertEqual(objects[key], model)

    def test_save(self):
        """
        Test that the save() method saves objects to a file.

        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        # Check if the file exists
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

        # Check if the file is not empty
        self.assertTrue(os.path.getsize(
            self.storage._FileStorage__file_path) > 0)

    def test_reload(self):
        """
        Test that the reload() method reloads objects from a file.

        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        # Clear the objects in memory
        self.storage._FileStorage__objects = {}

        # Reload the objects from the file
        self.storage.reload()

        objects = self.storage.all()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, objects)
        self.assertEqual(objects[key].id, model.id)
        self.assertEqual(objects[key].created_at, model.created_at)
        self.assertEqual(objects[key].updated_at, model.updated_at)


if __name__ == '__main__':
    unittest.main()
