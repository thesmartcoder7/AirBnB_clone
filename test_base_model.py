#!/usr/bin/python3
"""
A sample script demonstrating the usage of the BaseModel class.

"""

from models.base_model import BaseModel

# Create a new instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Print the string representation of my_model
print(my_model)

# Save my_model and update the updated_at attribute
my_model.save()

# Print the updated string representation of my_model
print(my_model)

# Get the dictionary representation of my_model
my_model_json = my_model.to_dict()

# Print the dictionary representation of my_model
print(my_model_json)

# Print the JSON of my_model
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))
