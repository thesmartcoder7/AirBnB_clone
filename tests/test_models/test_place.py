#!/usr/bin/python3
"""
Contains the unit tests for the Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.place = None

    def test_attributes(self):
        """
        Test the attributes of the Place class.
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

        self.place.city_id = "city123"
        self.place.user_id = "user123"
        self.place.name = "Cozy Apartment"
        self.place.description = "A cozy and comfortable apartment."
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(self.place.city_id, "city123")
        self.assertEqual(self.place.user_id, "user123")
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.description,
                         "A cozy and comfortable apartment.")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == "__main__":
    unittest.main()
