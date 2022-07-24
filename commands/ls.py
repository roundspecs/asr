import click
from models.task_list import TaskList

@click.command()
def ls():
    task_list = TaskList.from_json_file()
    click.echo(task_list.tree_str())