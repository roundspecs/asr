import click

from commands.do import do
from commands.stop import stop
from commands.ls import ls
from commands.add import add


@click.group()
def main():
    """A time tracking and journaling tool"""
    pass


main.add_command(do)
main.add_command(stop)
main.add_command(ls)
main.add_command(add)
