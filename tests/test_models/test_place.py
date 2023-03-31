#!/usr/bin/python3
"""
Place Unittest
"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Place Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_place = Place()
        self.assertIsInstance(my_place, Place)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_place = Place()
        self.assertEqual(type(my_place.id), str)
        self.assertIsInstance(my_place.created_at, datetime)
        self.assertIsInstance(my_place.updated_at, datetime)
        self.assertEqual(type(my_place.name), str)
        self.assertEqual(type(my_place.city_id), str)
        self.assertEqual(type(my_place.user_id), str)
        self.assertEqual(type(my_place.description), str)
        self.assertEqual(type(my_place.number_rooms), int)
        self.assertEqual(type(my_place.number_bathrooms), int)
        self.assertEqual(type(my_place.max_guest), int)
        self.assertEqual(type(my_place.price_by_night), int)
        self.assertEqual(type(my_place.latitude), float)
        self.assertEqual(type(my_place.longitude), float)
        self.assertEqual(type(my_place.amenity_ids), list)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_place = Place()
        my_place.name = "My First Model"
        my_place.my_number = 89
        self.assertEqual(type(str(my_place)), str)

    def test_save(self):
        """Testing the save method"""
        my_place = Place()
        self.assertEqual(type(str(my_place)), str)
        my_place.save()
        self.assertEqual(type(str(my_place)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_place = Place()
        place_dict = my_place.to_dict()
        new_place = Place(**place_dict)
        self.assertIsInstance(new_place, Place)
        self.assertEqual(type(new_place.id), str)
        self.assertIsInstance(new_place.created_at, datetime)
        self.assertIsInstance(new_place.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
