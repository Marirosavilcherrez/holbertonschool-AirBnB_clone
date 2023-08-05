#!/usr/bin/python3
import cmd
import sys
"""Create a program that contains the entry point of the
command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Class of the console"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """don´t do anything"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
