#!/usr/bin/python3
"""Module defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """the class User that inherits from BaseModel

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization point inherit super class"""
        super().__init__(*args, **kwargs)
