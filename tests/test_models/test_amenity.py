#!/usr/bin/python3
"""
Contains the unit tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.amenity = None

    def test_attributes(self):
        """
        Test the attributes of the Amenity class.
        """
        self.assertEqual(self.amenity.name, "")

        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")


if __name__ == "__main__":
    unittest.main()
