#!/usr/bin/python3
"""
Module for the HBNB command interpreter.

This module implements the HBNBCommand class, which serves as the command interpreter.

"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for HBNB.

    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id.
        Usage: create <class name>

        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [class name]

        """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(obj) for obj in objects.values()
                      if type(obj).__name__ == class_name])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                instance = objects[key]
                attribute_name = args[2]
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

    def help_create(self):
        """
        Help message for the create command.

        """
        print("Create a new instance of BaseModel, save it (to the JSON file), and print the id")

    def help_show(self):
        """
        Help message for the show command.

        """
        print(
            "Print the string representation of an instance based on the class name and id")

    def help_destroy(self):
        """
        Help message for the destroy command.

        """
        print("Delete an instance based on the class name and id (save the change into the JSON file)")

    def help_all(self):
        """
        Help message for the all command.

        """
        print("Print all string representations of all instances based or not on the class name")

    def help_update(self):
        """
        Help message for the update command.

        """
        print("Update an instance based on the class name and id by adding or updating an attribute")

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
