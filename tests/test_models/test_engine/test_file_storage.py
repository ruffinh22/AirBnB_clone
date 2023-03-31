#!/usr/bin/python3
"""
Module for testing file storage
"""
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """FileStorage test class"""
    def test_instance(self):
        """Testing instsnce of FileStorage Class"""
        store = FileStorage()
        self.assertIsInstance(store, FileStorage)

    def test_all(self):
        """Testing the all method of FileStorage"""
        store = FileStorage()
        all_objs = store.all()
        self.assertEqual(type(all_objs), dict)

    def test_save(self):
        """Testing the save method of FileStorage"""
        store = BaseModel()
        store.name = "Storage"
        store.size = 64
        store.save()
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)

    def test_reload(self):
        """Testing the reload method of FileStorage"""
        store = BaseModel()
        store.name = "Storage"
        store.size = 64
        store.save()
        storage.reload()
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)


if __name__ == "__main__":
    unittest.main()
