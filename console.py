#!/usr/bin/python3
"""
Module for the HBNB command interpreter.

This module implements the HBNBCommand class, which serves as
the command interpreter.

"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for HBNB.

    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when the end-of-file character is
        encountered (Ctrl + D).

        """
        print()
        return True

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
        print(
            "Exit the program when the end-of-file"
            "character is encountered (Ctrl + D)"
        )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
