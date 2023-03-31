#!/usr/bin/python3
"""
User Unittest
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    User Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_user = User()
        self.assertEqual(type(my_user.id), str)
        self.assertIsInstance(my_user.created_at, datetime)
        self.assertIsInstance(my_user.updated_at, datetime)
        self.assertEqual(type(my_user.email), str)
        self.assertEqual(type(my_user.password), str)
        self.assertEqual(type(my_user.first_name), str)
        self.assertEqual(type(my_user.last_name), str)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_user = User()
        my_user.name = "My First Model"
        my_user.my_number = 89
        self.assertEqual(type(str(my_user)), str)

    def test_save(self):
        """Testing the save method"""
        my_user = User()
        self.assertEqual(type(str(my_user)), str)
        my_user.save()
        self.assertEqual(type(str(my_user)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_user = User()
        user_dict = my_user.to_dict()
        new_user = User(**user_dict)
        self.assertIsInstance(new_user, User)
        self.assertEqual(type(new_user.id), str)
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
