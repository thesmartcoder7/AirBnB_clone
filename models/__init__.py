#!/usr/bin/python3
"""
Module for initializing the storage and reloading data.

This module initializes the FileStorage instance and
reloads data from the JSON file.

"""

from models.engine.file_storage import FileStorage

# Initialize the storage
storage = FileStorage()

# Reload data from the JSON file
storage.reload()
