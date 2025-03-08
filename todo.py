import click  # to create a cli
import json  # to save and load tasks from a file
import os  # to check if the file exists

TODO_FILE = "todo.json"


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r")as file:
        return json.load(file)


def save_tasks(task):
    with open(TODO_FILE, "w")as file:
        json.dump(task, file, indent=4)


@click.group()
def cli():
    """Simple Todo List Manager"""
    pass


@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")


@click.command()
def list():
    """List All the Tasks """
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index} {task["task"]} [{status}]")


@click.command()
@click.argument("task_number", type=int)
def complete_task(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task:{task_number} completed")
    else:
        click.echo(f"Invalid task number: {task_number}")


@click.command()
@click.argument("task_number", type=int)
def delete_task(task_number):
    """Delete a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number-1)
        save_tasks(tasks)
        click.echo(f"Removed Task: {removed_task["task"]}")
    else:
        click.echo(f"Invalid task number: {task_number}")


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete_task)
cli.add_command(delete_task)

if __name__ == "__main__":
    cli()
