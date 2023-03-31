#!/usr/bin/python3
"""
City Unittest
"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    City Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_city = City()
        self.assertIsInstance(my_city, City)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_city = City()
        self.assertEqual(type(my_city.id), str)
        self.assertIsInstance(my_city.created_at, datetime)
        self.assertIsInstance(my_city.updated_at, datetime)
        self.assertEqual(type(my_city.name), str)
        self.assertEqual(type(my_city.state_id), str)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_city = City()
        my_city.name = "My First Model"
        my_city.my_number = 89
        self.assertEqual(type(str(my_city)), str)

    def test_save(self):
        """Testing the save method"""
        my_city = City()
        self.assertEqual(type(str(my_city)), str)
        my_city.save()
        self.assertEqual(type(str(my_city)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_city = City()
        city_dict = my_city.to_dict()
        new_city = City(**city_dict)
        self.assertIsInstance(new_city, City)
        self.assertEqual(type(new_city.id), str)
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
