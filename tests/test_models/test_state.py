#!/usr/bin/python3
"""
State Unittest
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    State Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_state = State()
        self.assertEqual(type(my_state.id), str)
        self.assertIsInstance(my_state.created_at, datetime)
        self.assertIsInstance(my_state.updated_at, datetime)
        self.assertEqual(type(my_state.name), str)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_state = State()
        my_state.name = "My First Model"
        my_state.my_number = 89
        self.assertEqual(type(str(my_state)), str)

    def test_save(self):
        """Testing the save method"""
        my_state = State()
        self.assertEqual(type(str(my_state)), str)
        my_state.save()
        self.assertEqual(type(str(my_state)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_state = State()
        state_dict = my_state.to_dict()
        new_state = State(**state_dict)
        self.assertIsInstance(new_state, State)
        self.assertEqual(type(new_state.id), str)
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
