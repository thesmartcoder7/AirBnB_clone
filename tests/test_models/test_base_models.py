import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.model = BaseModel()

    def test_id(self):
        """
        Test the 'id' attribute of the BaseModel class.
        """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertIsInstance(self.model.id, str)
        self.assertNotEqual(self.model.id, '')

    def test_created_at(self):
        """
        Test the 'created_at' attribute of the BaseModel class.
        """
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """
        Test the 'updated_at' attribute of the BaseModel class.
        """
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """
        Test the 'save' method of the BaseModel class.
        """
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test the 'to_dict' method of the BaseModel class.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
