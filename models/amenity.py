#!/usr/bin/python3

"""
amenity.py
====================================
Module for the Amenity class.

Classes:
- Amenity

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Attributes:
        name (str): The name of the amenity.

    """

    name = ""
