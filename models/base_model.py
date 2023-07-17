#!/usr/bin/python3

"""
Module for the BaseModel class.

Classes:
- BaseModel

"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that defines common attributes and methods for other classes.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last updated.

    Methods:
        __init__(*args, **kwargs): Initializes a new instance of BaseModel.
        __str__(): Returns a string representation of the BaseModel instance.
        save(): Updates the 'updated_at' attribute with the current date and time.
        to_dict(): Returns a dictionary representation of the BaseModel instance.

    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key != "created_at" and key != "updated_at":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: The string representation of the BaseModel instance.

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date and time.

        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary representation of the BaseModel instance.

        """
        copy = self.__dict__.copy()
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
