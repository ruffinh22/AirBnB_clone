#!/usr/bin/python3
"""
BaseModel Unittest
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    BaseModel Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(type(str(my_model)), str)

    def test_save(self):
        """Testing the save method"""
        my_model = BaseModel()
        self.assertEqual(type(str(my_model)), str)
        my_model.save()
        self.assertEqual(type(str(my_model)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertEqual(type(model_dict), dict)

    def test_instance_with_kwargs(self):
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(type(new_model.id), str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
