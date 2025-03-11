# Todo CLI

A simple command-line interface (CLI) for managing a to-do list using Python and the `click` library.

## Features
- Add tasks
- List all tasks with status
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON

## Requirements
Make sure you have Python installed on your system. This script uses the `click` library, which you can install using:

```sh
pip install click
```

## Installation
1. Clone this repository or download the `todo.py` file.
2. Ensure you have `click` installed.

## Usage
Navigate to the directory containing `todo.py` and run the following commands:

### Add a Task
```sh
python todo.py add "Your Task Here"
```
Example:
```sh
python todo.py add "Buy Grocery for Sehri and Iftari"
```

### List All Tasks
```sh
python todo.py list
```
Output Example:
```
1 Buy Grocery for Sehri and Iftari [✅]
```

### Mark a Task as Completed
```sh
python todo.py complete-task <task_number>
```
Example:
```sh
python todo.py complete-task 1
```

### Delete a Task
```sh
python todo.py delete-task <task_number>
```
Example:
```sh
python todo.py delete-task 1
```

## Data Storage
The tasks are stored in `todo.json` in the following format:
```json
[
  {
    "task": "Buy Grocery for Sehri and Iftari",
    "done": true
  }
]
```

## Notes
- Task numbers start from `1` in the CLI.
- The JSON file maintains task data between script runs.

## License
This project is open-source and free to use.

## Author
Developed by Hafiz Siddiqui.
