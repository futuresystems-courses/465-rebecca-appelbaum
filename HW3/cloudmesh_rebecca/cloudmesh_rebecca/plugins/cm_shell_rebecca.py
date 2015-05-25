from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_rebecca.command_rebecca import command_rebecca


class cm_shell_rebecca:

    def activate_cm_shell_rebecca(self):
        self.register_command_topic('mycommands', 'rebecca')

    @command
    def do_rebecca(self, args, arguments):
        """
        ::

          Usage:
              rebecca NAME

          tests via ping if the host ith the give NAME is reachable

          Arguments:

            NAME      Name of the machine to test

          Options:

             -v       verbose mode

        """
        # pprint(arguments)

        if arguments["NAME"] is None:
            Console.error("Please specify a host name")
        else:
            host = arguments["NAME"]
            Console.info("trying to reach {0}".format(host))
            status = command_rebecca.status(host)
            if status:
                Console.info("machine " + host + " has been found. ok.")
            else:
                Console.error("machine " + host + " not reachable. error.")
        pass

if __name__ == '__main__':
    command = cm_shell_rebecca()
    command.do_rebecca("iu.edu")
    command.do_rebecca("iu.edu-wrong")
