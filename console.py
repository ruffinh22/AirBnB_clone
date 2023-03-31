#!/usr/bin/python3
"""
A module that works as a console or entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A class that implements the command interpreter
    """
    prompt = '(hbnb) '
    file = None
    models = [
            'BaseModel',
            'User',
            'Place',
            'State',
            'City',
            'Amenity',
            'Review'
            ]
    class_ids = []
    for key in storage.all():
        class_ids.append(key.split(".")[1])

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        """
        Exit the command interpreter
        """
        quit()

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        """
        Exit the command interpreter
        """
        quit()

    def emptyline(self):
        """
        Do nothing after an empty line
        """
        pass

    def do_create(self, arg):
        'Command to create a new instance of BaseModel and save it\n'\
                'Ex: (hbnb) create BaseModel\n'
        """
        Create and save a new instance of BaseModel
        """
        class_name = arg
        if len(class_name) == 0:
            print("** class name missing **")
        elif len(class_name) != 0 and class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            if class_name == "BaseModel":
                instance = BaseModel()
            elif class_name == "User":
                instance = User()
            elif class_name == "Place":
                instance = Place()
            elif class_name == "State":
                instance = State()
            elif class_name == "City":
                instance = City()
            elif class_name == "Amenity":
                instance = Amenity()
            elif class_name == "Review":
                instance = Review()
            instance.save()
            HBNBCommand.class_ids.append(instance.id)
            print(instance.id)

    def do_show(self, arg):
        'Prints the string representation of an instance '\
                'based on the class name and id\n'\
                'Ex: (hbnb) show BaseModel 1234-1234-1234\n'
        """
        Print the string representation of an instance
        """
        if " " in arg:
            class_name = arg.split()[0]
            class_id = arg.split()[1]
        else:
            class_name = arg
            class_id = ""

        key = "{0}.{1}".format(class_name, class_id)
        if len(class_name) == 0:
            print("** class name missing **")
        elif len(class_name) != 0 and class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif class_name in HBNBCommand.models and len(class_id) == 0:
            print("** instance id missing **")
        elif key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id and save\n'\
                'Ex: (hbnb) destroy BaseModel 1234-1234-1234\n'
        """
        Deletes an instance based on the class name and id
        """
        if " " in arg:
            class_name = arg.split()[0]
            class_id = arg.split()[1]
        else:
            class_name = arg
            class_id = ""
        key = "{0}.{1}".format(class_name, class_id)
        if len(class_name) == 0:
            print("** class name missing **")
        elif len(class_name) != 0 and class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif class_name in HBNBCommand.models and len(class_id) == 0:
            print("** instance id missing **")
        elif key not in storage.all():
            print("** no instance found **")
        else:
            storage.all().pop(key)
            storage.save()
            HBNBCommand.class_ids.remove(class_id)

    def do_all(self, arg):
        'Prints all string representation of all instances based '\
                'or not on the class name\nEx: (hbnb) all BaseModel or\n'\
                '    (hbnb) all\n'
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        class_name = arg

        if len(class_name) != 0 and class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            all_instances = []
            for obj in storage.all().values():
                if class_name == obj.__class__.__name__:
                    all_instances.append(str(obj))
                elif len(class_name) == 0:
                    all_instances.append(str(obj))
            print(all_instances)

    def do_update(self, arg):
        'Updates an instance based on the class name and id by adding '\
                'or updating attribute and saves the change\n'\
                'Ex: (hbnb) update BaseModel 1234-1234-1234 email '\
                '"aibnb@mail.com"\n'
        """
        Updates an instance based on the class name and id
        by adding or updating attribute and saves the change
        """
        if " " in arg:
            args = arg.split()
            if len(args) == 2:
                class_name = args[0]
                class_id = args[1]
                attr_name = ""
                attr_value = ""
            elif len(args) == 3:
                args = arg.split(" ", 2)
                class_name = args[0]
                class_id = args[1]
                attr_name = args[2]
                attr_value = ""
            elif len(args) == 4:
                class_name = args[0]
                class_id = args[1]
                attr_name = args[2]
                attr_value = args[3]
            elif len(args) > 4 and arg[3][-1] == "\"":
                args = arg.split(" ", 3)
                class_name = args[0]
                class_id = args[1]
                attr_name = args[2]
                attr_value = args[3]
            elif len(args) > 4 and args[3][0] == "\"":
                args = arg.split(" ", 3)
                class_name = args[0]
                class_id = args[1]
                attr_name = args[2]
                value_index = args[3].index("\"", 1)
                attr_value = args[3][:value_index]
            elif len(args) > 4:
                class_name = args[0]
                class_id = args[1]
                attr_name = args[2]
                attr_value = args[3].split()[0]

        else:
            class_name = arg
            class_id = ""
            attr_name = ""
            attr_value = ""

        if len(class_name) == 0:
            print("** class name missing **")
        elif len(class_name) != 0\
                and class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
        elif len(class_name) != 0\
                and class_name in HBNBCommand.models\
                and len(class_id) == 0:
            print("** instance id missing **")
        elif len(class_name) != 0\
                and class_name in HBNBCommand.models\
                and len(class_id) != 0\
                and class_id not in HBNBCommand.class_ids:
            print("** no instance found **")
        elif len(class_name) != 0\
                and class_name in HBNBCommand.models\
                and len(class_id) != 0\
                and class_id in HBNBCommand.class_ids\
                and len(attr_name) == 0:
            print("** attribute name missing **")
        elif len(class_name) != 0\
                and class_name in HBNBCommand.models\
                and len(class_id) != 0\
                and class_id in HBNBCommand.class_ids\
                and len(attr_name) != 0\
                and len(attr_value) == 0:
            print("** value missing **")
        else:
            key = "{0}.{1}".format(class_name, class_id)
            attr_value = attr_value.strip('\"')
            setattr(
                    storage.all()[key],
                    attr_name,
                    attr_value
                    )
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
