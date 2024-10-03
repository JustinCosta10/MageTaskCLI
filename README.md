
# MageTask CLI

Mage Task Manager is a simple CLI tool that allows you to manage your weekly tasks. You can add tasks, view them, and reset all tasks with simple commands.
These instructions use bash commands. The tool should work with Windows but there may be some unforeseen differences in setup.

My goals with creating this tool were mostly to learn SQLite database integration into Python and the Python Click library.
However, I have found it useful when installed into the path for quickly tracking weekly tasks.

I do not include instructions for path installation because of vast differences in instructions based on OS and setup,
but the program is most useful when it can be used from any location in the terminal with the Click commands.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/magetask.git
   ```

2. Create a virtual environment within the MageTask directory:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependency:

   ```bash
    pip install click
   ```

## Usage

With Path Install:
For regular use, the program can also be installed directly into the path,
but these instructions are just for getting it working in the folder.
If installed correctly into the path, terminal commands like this should work:
```bash
mage add "task description" day time
```
Without path Install:
To use the Mage Task Manager, you can use the following commands:

```bash
python mage.py add "task description" day time
```

### Add a Task

- `task description`: The task description (up to 25 characters).
- `day`: The day of the week (e.g., `mon`, `tue`, `wed`).
- `time`: The time in regular format (e.g., `1130a`, `430p`).

**Example:**

```bash
python mage.py add "walk the dog" wed 1130a
```

### List All Tasks

```bash
python mage.py view
```

This command will display all the tasks sorted by day and time.

### Reset All Tasks

```bash
python mage.py reset
```

This command will delete all the tasks from the database. This can clear the week when task tracking a new week of work.

## Notes

- The database will be automatically created on the first run.
- Tasks are limited to 25 characters, and days must be entered in short form (e.g., `mon`, `tue`, `wed`).
