#!/usr/bin/python3
"""
Amenity Unittest
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Amenity Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_amenity = Amenity()
        self.assertEqual(type(my_amenity.id), str)
        self.assertIsInstance(my_amenity.created_at, datetime)
        self.assertIsInstance(my_amenity.updated_at, datetime)
        self.assertEqual(type(my_amenity.name), str)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_amenity = Amenity()
        my_amenity.name = "My First Model"
        my_amenity.my_number = 89
        self.assertEqual(type(str(my_amenity)), str)

    def test_save(self):
        """Testing the save method"""
        my_amenity = Amenity()
        self.assertEqual(type(str(my_amenity)), str)
        my_amenity.save()
        self.assertEqual(type(str(my_amenity)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_amenity = Amenity()
        amenity_dict = my_amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(type(new_amenity.id), str)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
