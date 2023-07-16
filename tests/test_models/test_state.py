#!/usr/bin/python3
"""
Contains the unit tests for the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.state = None

    def test_attributes(self):
        """
        Test the attributes of the State class.
        """
        self.assertEqual(self.state.name, "")

        self.state.name = "California"

        self.assertEqual(self.state.name, "California")


if __name__ == "__main__":
    unittest.main()
