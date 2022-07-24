import typer

from models.task_list import TaskList

app = typer.Typer()


@app.command()
def add(emmet_abbr: str):
    """Add a new task"""
    task_list = TaskList.from_json_file()
    added_task_list = task_list.add_task_as_emmet(emmet_abbr)
    print("Added tasks:")
    print(added_task_list.tree_str())


@app.command(name="ls")
def list():
    """List all the task in task list"""
    task_list = TaskList.from_json_file()
    print(task_list.tree_str())


@app.command(name="rm")
def remove(emmet_abbr: str):
    """Remove a task"""
    task_list = TaskList.from_json_file()
    removed_task_list = task_list.remove_task_as_emmet(emmet_abbr)
    print("Removed tasks:")
    print(removed_task_list.tree_str())
