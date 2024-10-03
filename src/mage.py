#!/usr/bin/env python3
import click
from task_manage import TaskManage

@click.group()
def mage():
    """Task management CLI."""
    pass

@mage.command()
@click.argument('task_description')
@click.argument('task_day')
@click.argument('task_time')
def add(task_description, task_day, task_time):
    """Add a new task."""
    task_manager = TaskManage()
    task_manager.create_task(task_description, task_day, task_time)

@mage.command()
def view():
    """View all tasks."""
    task_manager = TaskManage()
    tasks = task_manager.pull_tasks()
    click.echo(tasks)

@mage.command()
@click.argument('task_description')
def delete(task_description):
    """Delete an existing task."""
    task_manager = TaskManage()
    task_manager.delete_task(task_description)
    click.echo(f"Task '{task_description}' deleted.")

@mage.command()
def reset():
    """Reset all tasks."""
    task_manager = TaskManage()
    task_manager.reset_tasks()
    click.echo("All tasks have been reset.")

if __name__ == "__main__":
    mage()
