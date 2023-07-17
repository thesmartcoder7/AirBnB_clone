#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review

import cmd
import re
from shlex import split

# A global constant since both functions within and outside uses it.
all_classes = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]


def parse(arg):
    """
    Parse the given argument into a list of arguments.

    Args:
        arg (str): The argument to parse.

    Returns:
        list: A list of parsed arguments.

    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """
    Check if the arguments are valid.

    Args:
        args (str): The string containing the arguments passed to a command.

    Returns:
        list or None: The list of arguments if valid, otherwise None.

    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in all_classes:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """
    The class that implements the console for the AirBnB clone web application.
    """

    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """
        Command to be executed when an empty line + <ENTER> key is entered.

        """
        pass

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid.

        Args:
            arg (str): The input argument.

        Returns:
            bool: False to indicate the command is not recognized.

        """
        actions = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in actions:
                    call = "{} {}".format(arg1[0], command[1])
                    return actions[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, argv):
        """
        Handle the EOF (End-of-File) signal to exit the program.

        Args:
            argv: The argument.

        Returns:
            bool: True to indicate the program should exit.

        """
        print("")
        return True

    def do_quit(self, argv):
        """
        Handle the quit command.

        Args:
            argv: The argument.

        Returns:
            bool: True to indicate the program should exit.

        """
        return True

    def do_create(self, argv):
        """
        Create a new instance of BaseModel, save it to a JSON file,
        and print the id.

        Args:
            argv (str): The argument.

        """
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """
        Print the string representation of an instance based on
        the class name and id.

        Args:
            argv (str): The argument.

        """
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_all(self, argv):
        """
        Print the string representation of all instances based on
        the class name.

        Args:
            argv (str): The argument.

        """
        arg_list = split(argv)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in all_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects if arg_list[0] in str(obj)])

    def do_destroy(self, argv):
        """
        Delete a class instance based on the name and given id.

        Args:
            argv (str): The argument.

        """
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, argv):
        """
        Update an instance based on the class name and id by adding
        or updating attribute.

        Args:
            argv (str): The argument.

        """
        arg_list = HBNBCommand.parse(argv)
        objdict = models.storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = valtype(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        models.storage.save()

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class.

        Args:
            arg (str): The argument.

        """
        arg1 = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
