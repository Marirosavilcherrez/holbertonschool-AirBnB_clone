#!/usr/bin/python3
"""Create a program that contains the entry point of the
command interpreter"""
import cmd
import sys
import json
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Class of the console"""
    """This is a module of the console"""
    prompt = '(hbnb)'
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
    }

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

    def do_create(self, name):
        if len(name) == 0:
            print("** class name missing **")
        elif name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        else:
            novo = eval("{}()".format(name))
            novo.save()
            print(novo.id)

    def do_show(self, arg):
        id_cls = arg.split()
        if not id_cls:
            print("** class name missing **")
            return
        if id_cls[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(id_cls) < 2:
            print("** instance id missing **")
            return
        else:
            link = "{}.{}".format(id_cls[0], id_cls[1])
            full_obj = storage.all()
            if link not in full_obj:
                print("** no instance found **")
            else:
                print(f"{full_obj[link]}")

    def do_destroy(self, argument):
        destr_id = argument.split()
        if len(destr_id) == 0:
            print("** class name missing **")
            return
        if destr_id[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(destr_id) < 2:
            print("** instance id missing **")
            return
        else:
            k = "{}.{}".format(destr_id[0], destr_id[1])
            full_obj = storage.all()
            if k not in full_obj:
                print("** no instance found **")
            else:
                del full_obj[k]
                storage.save()

    def do_all(self, arg):
        imp_id = arg.split()
        if len(imp_id) > 0 and imp_id[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(imp_id) > 0 and imp_id[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(imp_id) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, args):
        upd_cls = args.split()
        if not upd_cls:
            print("** class name missing **")
            return
        if upd_cls[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(upd_cls) < 2:
            print("** instance id missing **")
            return

        upd_obj = storage.all()
        key = upd_cls[0] + '.' + upd_cls[1]

        if key not in upd_obj:
            print("** no instance found **")
            return
        if len(upd_cls) < 3:
            print("** attribute name missing **")
            return
        if len(upd_cls) < 4:
            print("** value missing **")
            return
        setattr(upd_obj[key], upd_cls[2], upd_cls[3])
        upd_obj[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
