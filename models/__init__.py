#!/usr/bin/python3
"""
The init module for models
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
