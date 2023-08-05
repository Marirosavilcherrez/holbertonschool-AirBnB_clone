#!/usr/bin/python3
import cmd
import sys
"""Create a program that contains the entry point of the
command interpreter"""
"""This is a module of the console"""


class HBNBCommand(cmd.Cmd):
    """Class of the console"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        This comand exit the program
        
        Parameters:
            arg: the argument
        """
        return True

    def do_EOF(self, arg):
        """
        This comand exit the program
        
        Parameters:
            arg: the argument
        """
        return True

    def emptyline(self):
        """don´t do anything"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
