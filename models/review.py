#!/usr/bin/python3

"""
review.py
====================================
Module for the Review class.

Classes:
- Review

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The place ID (Place.id) of the review.

        user_id (str): The user ID (User.id) of the review.

        text (str): The text content of the review.

    """

    place_id = ""
    user_id = ""
    text = ""
