#!/usr/bin/python3
"""
A module that implements file storage
"""
import json
import os


class FileStorage(object):
    """
    A class that serializes instances to a JSON file and
    deserializes JSON file to instances

    Attr:
        __file_path (str): path to the JSON file
        __object (dict): stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method that returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        A method that sets in __objects the obj with
        its key as <obj class name>.id

        Args:
            obj (object): object to be stored
        """
        key = "{}.{}".format(
                obj.__class__.__name__,
                obj.id
                )
        FileStorage.__objects[key] = obj

    def save(self):
        """
        A method that serializes __objects to a JSON file
        """
        objdict = {}
        for objects in FileStorage.__objects:
            objdict[objects] = FileStorage.__objects[objects].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objdict, f)

    def reload(self):
        """
        A method that deserializes the JSON file to
        __objects if the file exists
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        my_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }
        if not os.path.exists(FileStorage.__file_path):
            return
        else:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objects = json.load(f)
                FileStorage.__objects = {}
                for key in objects:
                    name = key.split(".")[0]
                    FileStorage.__objects[key] = my_dict[name](**objects[key])
