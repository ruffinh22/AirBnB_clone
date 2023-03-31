#!/usr/bin/python3
"""
A module containing a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
