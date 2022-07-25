import typer
from models.journal import Journal
from rich import print
from models.task_list import TaskList

app = typer.Typer()


@app.command()
def add(emmet_abbr: str):
    """Add a new task"""
    task_list = TaskList.load()
    added_task_list = task_list.add_task_as_emmet(emmet_abbr)
    print("Added tasks:")
    print(added_task_list.tree_str())


@app.command(name="ls")
def list():
    """List all the task in task list"""
    task_list = TaskList.load()
    print(task_list.tree_str())


@app.command(name="rm")
def remove(emmet_abbr: str):
    """Remove a task"""
    task_list = TaskList.load()
    removed_task_list = task_list.remove_task_as_emmet(emmet_abbr)
    print("Removed tasks:")
    print(removed_task_list.tree_str())


@app.command()
def do(task_path: str):
    """Start a task"""
    # TODO
    journal = Journal.load()
    journal.start_task(task_path)


@app.command()
def stop():
    """Start a task"""
    # TODO
    journal = Journal.load()
    journal.stop_task()
