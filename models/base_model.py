#!/usr/bin/python3
"""
A module that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel(object):
    """
    A class that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of an instance

        Attr:
            id (str): a unique id for each instance of the BaseModel class
            created_at (datetime): datetime when an instance is created
            updated_at (datetime): datetime when an instance is created
                                and updated each time the object is changed
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            kwargs_keys = list(kwargs.keys())
            for key in kwargs_keys:
                if key == '__class__':
                    pass
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            storage.new(self)

    def __str__(self):
        """
        Overriding the str method
        """
        return "[{0}] ({1}) {2}".format(self.__class__.__name__,
                                        self.id,
                                        self.__dict__
                                        )

    def save(self):
        """
        A method that updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        A method that returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
