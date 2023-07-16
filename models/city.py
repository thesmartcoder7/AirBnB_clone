#!/usr/bin/python3

"""
city.py
====================================
Module for the City class.

Classes:
- City

"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): The state ID (State.id) of the city.

        name (str): The name of the city.

    """

    state_id = ""
    name = ""
