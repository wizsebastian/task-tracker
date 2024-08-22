# Task Tracker CLI

## Overview
This is a Command Line Interface (CLI) application for tracking tasks, inspired by the project idea from [roadmap.sh](https://roadmap.sh/projects/task-tracker). As a beginner Python developer (with only 3 weeks of experience, only in python lol), I created this project to practice and improve my Python skills.

## Features
- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as todo, in-progress, or done
- List all tasks
- List tasks by status

## Installation
1. Clone this repository
2. Navigate to the project directory
3. Run `pip install -e .` to install the package in editable mode

## Usage
After installation, you can use the `task-cli` command followed by various subcommands:

- `task-cli add "Task description"` - Add a new task
- `task-cli update <task_id> "Updated description"` - Update a task
- `task-cli delete <task_id>` - Delete a task
- `task-cli mark-todo <task_id>` - Mark a task as todo
- `task-cli mark-in-progress <task_id>` - Mark a task as in-progress
- `task-cli mark-done <task_id>` - Mark a task as done
- `task-cli list` - List all tasks
- `task-cli list <status>` - List tasks by status (todo, in-progress, or done)

## Project Structure
- `setup.py`: Package configuration
- `task_cli/`: Main package directory
  - `__init__.py`: Package initializer
  - `cli.py`: Contains the main application logic

## Learning Journey
As a newcomer to Python, this project has been a great learning experience. I've practiced concepts such as:
- Object-Oriented Programming
- File I/O operations
- JSON data handling
- Command-line argument parsing
- Error handling

## Feedback and Improvements
I'm always looking to improve my coding skills. If you have any suggestions or feedback, please feel free to open an issue or submit a pull request!
