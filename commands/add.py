import click

@click.command()
@click.argument('task_path')
def add(task_path: str):
    """Add a new task"""
    task_path = task_path.strip('/').split('/')
    click.echo(task_path)