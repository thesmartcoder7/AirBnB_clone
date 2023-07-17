#!/usr/bin/python3
"""
Contains the unit tests for the console module.
"""

import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up the test environment.
        """
        self.console = None

    def test_create(self):
        """
        Test the create command.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(output.getvalue().strip()) == 36)

    def test_show(self):
        """
        Test the show command.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(obj_id in output.getvalue().strip())

    def test_all(self):
        """
        Test the all command.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("all BaseModel")
            self.assertTrue(obj_id in output.getvalue().strip())

    def test_destroy(self):
        """
        Test the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertFalse(obj_id in storage.all())

    def test_update(self):
        """
        Test the update command.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue("test" in output.getvalue().strip())

    def test_count(self):
        """
        Test the count command.
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("count BaseModel")


if __name__ == "__main__":
    unittest.main()
