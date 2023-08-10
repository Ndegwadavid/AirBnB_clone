#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()