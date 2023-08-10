#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of an object."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        print()
        return True

    def do_show(self, arg):


    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
