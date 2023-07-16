#!/usr/bin/python3
"""
console.py
====================================
Entry point for the command interpreter.

"""

import cmd
import sys
import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.

    Attributes:
        prompt (str): The prompt to display for user input.

    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered.

        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when the end-of-file character is encountered (Ctrl + D).

        """
        print()
        return True

    def help_quit(self):
        """
        Help message for the quit command.

        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help message for the EOF command.

        """
        print("Exit the program when the end-of-file character is encountered (Ctrl + D)")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it (to the JSON file), and print the id.

        Usage: create <class name>

        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and id.

        Usage: show <class name> <id>

        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            instance = storage.all()[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id (save the change into the JSON file).

        Usage: destroy <class name> <id>

        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances based on the class name.

        Usage: all <class name> or all

        """
        if arg:
            class_name = arg
            if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
                return
            instances = [str(instance) for key, instance in storage.all().items()
                         if class_name in key]
        else:
            instances = [str(instance) for instance in storage.all().values()]
        print(instances)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating attributes.

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            instance = storage.all()[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3].strip('"')
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** no instance found **")

    def emptyline(self):
        """
        Do nothing when an empty line is entered.

        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
