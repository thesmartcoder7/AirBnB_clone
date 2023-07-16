#!/usr/bin/python3
"""
Contains the unit tests for the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.city = None

    def test_attributes(self):
        """
        Test the attributes of the City class.
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

        self.city.state_id = "state123"
        self.city.name = "New York"

        self.assertEqual(self.city.state_id, "state123")
        self.assertEqual(self.city.name, "New York")


if __name__ == "__main__":
    unittest.main()
