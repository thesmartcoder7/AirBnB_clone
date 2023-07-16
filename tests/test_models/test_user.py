#!/usr/bin/python3
"""
Contains the unit tests for the User class.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.user = None

    def test_attributes(self):
        """
        Test the attributes of the User class.
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
