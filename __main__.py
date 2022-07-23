import click

from commands.start import start
from commands.stop import stop
from commands.todos import todos
from commands.add import add

@click.group()
def cli():
    pass

cli.add_command(start)
cli.add_command(stop)
cli.add_command(todos)
cli.add_command(add)

if __name__ == "__main__":
    cli()