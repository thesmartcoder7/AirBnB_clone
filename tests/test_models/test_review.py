#!/usr/bin/python3
"""
Contains the unit tests for the Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.review = None

    def test_attributes(self):
        """
        Test the attributes of the Review class.
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

        self.review.place_id = "place123"
        self.review.user_id = "user123"
        self.review.text = "Great place to stay!"

        self.assertEqual(self.review.place_id, "place123")
        self.assertEqual(self.review.user_id, "user123")
        self.assertEqual(self.review.text, "Great place to stay!")


if __name__ == "__main__":
    unittest.main()
