#!/usr/bin/python3
"""
base_model.py

This module defines the BaseModel class that serves as a base class for other classes.

"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines common attributes and methods for other classes.

    Public instance attributes:
    - id: string - A unique identifier assigned using uuid when an instance is created.
    - created_at: datetime - The datetime when an instance is created.
    - updated_at: datetime - The datetime when an instance is last updated.

    Public instance methods:
    - save(): Updates the public instance attribute updated_at with the current datetime.
    - to_dict(): Returns a dictionary containing all keys/values of the instance.

    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        The id is generated using uuid.uuid4() and converted to a string.
        The created_at and updated_at attributes are set to the current datetime.

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        The string includes the class name, id, and instance attributes.

        Returns:
            str: A string representation of the BaseModel instance.

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        The dictionary contains all instance attributes, including the class name, id,
        created_at, and updated_at attributes.

        Returns:
            dict: A dictionary representation of the BaseModel instance.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
