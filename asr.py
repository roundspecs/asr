import click

from commands.start import start
from commands.stop import stop
from commands.todos import todos
from commands.add import add

@click.group()
def task():
    """Endpoint to add/remove/start/stop task"""
    pass

task.add_command(start)
task.add_command(stop)
task.add_command(todos)
task.add_command(add)

@click.group()
def main():
    pass

main.add_command(task)