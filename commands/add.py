import click
from models.task_list import TaskList

@click.command()
@click.argument('emmet_abbr')
def add(emmet_abbr: str):
    """Add a new task"""
    task_list = TaskList.from_json_file()
    added_tasks = task_list.add_task_as_emmet(emmet_abbr)
    # TODO: print added tasks