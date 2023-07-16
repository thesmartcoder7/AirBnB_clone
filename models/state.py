#!/usr/bin/python3

"""
state.py
====================================
Module for the State class.

Classes:
- State

"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Attributes:
        name (str): The name of the state.

    """

    name = ""
