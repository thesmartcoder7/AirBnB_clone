#!/usr/bin/python3

"""
place.py
====================================
Module for the Place class.

Classes:
- Place

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Attributes:
        city_id (str): The city ID (City.id) of the place.

        user_id (str): The user ID (User.id) of the place.

        name (str): The name of the place.

        description (str): The description of the place.

        number_rooms (int): The number of rooms in the place.

        number_bathrooms (int): The number of bathrooms in the place.

        max_guest (int): The maximum number of guests the place can
        accommodate.

        price_by_night (int): The price per night for the place.

        latitude (float): The latitude coordinate of the place.

        longitude (float): The longitude coordinate of the place.

        amenity_ids (list of str): The list of amenity IDs (Amenity.id)
        of the place.

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
