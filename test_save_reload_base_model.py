#!/usr/bin/python3
"""
A sample script demonstrating the usage of the BaseModel class
and the storage object.

"""

from models import storage
from models.base_model import BaseModel

# Reload all objects from the storage
all_objs = storage.all()

print("-- Reloaded objects --")
# Print the reloaded objects
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
# Create a new instance of BaseModel
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

# Save my_model and update the updated_at attribute
my_model.save()

# Print the string representation of my_model
print(my_model)
