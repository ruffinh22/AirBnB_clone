#!/usr/bin/python3
"""
Review Unittest
"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Review Test Class
    """
    def test_instance(self):
        """Testing created instances"""
        my_review = Review()
        self.assertIsInstance(my_review, Review)

    def test_attributes(self):
        """Testing class attributes from an instance"""
        my_review = Review()
        self.assertEqual(type(my_review.id), str)
        self.assertIsInstance(my_review.created_at, datetime)
        self.assertIsInstance(my_review.updated_at, datetime)
        self.assertEqual(type(my_review.place_id), str)
        self.assertEqual(type(my_review.user_id), str)
        self.assertEqual(type(my_review.text), str)

    def test_str_override(self):
        """Testing the print output of an instance"""
        my_review = Review()
        my_review.name = "My First Model"
        my_review.my_number = 89
        self.assertEqual(type(str(my_review)), str)

    def test_save(self):
        """Testing the save method"""
        my_review = Review()
        self.assertEqual(type(str(my_review)), str)
        my_review.save()
        self.assertEqual(type(str(my_review)), str)

    def test_to_dict(self):
        """Testing the to_dict method"""
        my_review = Review()
        review_dict = my_review.to_dict()
        new_review = Review(**review_dict)
        self.assertIsInstance(new_review, Review)
        self.assertEqual(type(new_review.id), str)
        self.assertIsInstance(new_review.created_at, datetime)
        self.assertIsInstance(new_review.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
