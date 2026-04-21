# Terminal Goal Tracker

A simple command-line application to track and manage your daily goals with persistent storage.

## Description

Terminal Goal Tracker is a Python-based CLI tool that helps you manage your goals efficiently. It allows you to add, check, and modify goals with their completion status. All goals are stored persistently using Python's pickle module.

## Features

- **Add Goals**: Create new goals with the ability to add multiple checks
- **Check Goals**: View all your goals and their completion status with color-coded output
- **Modify Goals**: Update the completion status of existing goals
- **Persistent Storage**: Goals are saved to a file and persist between sessions
- **Interactive Menu**: User-friendly command-line interface

## Requirements

- **Python 3.6 or higher**
- **No external dependencies** (uses only Python standard library)

### System Requirements
- Any OS that supports Python (Windows, macOS, Linux)
- Sufficient disk space for goal files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/slashSL07/terminal-goal-tracker.git
cd terminal-goal-tracker
```

2. No additional installation needed - just run the script!

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **Check Goals** - View all your goals and their completion status
2. **Add Goals** - Create new goals (you can add multiple checks at once)
3. **Modify Goals** - Update the completion status of existing goals

### Example Workflow

```
filename: my_goals
do you want to (1)check, (2) add, (3) modify: 2
num of checks: 2
add check: Exercise for 30 minutes
add check: Read a chapter of a book
any extra checks you want to add(y/n): n
do you want to continue(y/n): y

do you want to (1)check, (2) add, (3) modify: 1
goal Exercise for 30 minutes : completion 🟢 True
goal Read a chapter of a book : completion 🔴 False

do you want to continue(y/n): n
```

## Goal File Format

Goals are stored in pickle files with the `.goals` extension. The file contains a dictionary where:
- **Key**: Goal name (string)
- **Value**: Completion status (boolean - True/False)

## Color Output

- 🟣 **Purple** (`\033[35m`): Goal/Goal Completion label
- 🟢 **Green** (`\033[92m`): Completed goals (True)
- 🔴 **Red** (`\033[31m`): Incomplete goals (False)

## File Structure

```
terminal-goal-tracker/
├── main.py           # Main application file
├── README.md         # Project documentation
└── *.goals           # Goal files (created at runtime)
```

## How It Works

1. **Filename Input**: Enter a filename for your goals (automatically adds `.goals` extension)
2. **Pickle Storage**: Goals are serialized using Python's pickle module for persistence
3. **Interactive Menu**: Choose between checking, adding, or modifying goals
4. **Color-Coded Display**: Easy-to-read goal status with ANSI color codes

## Known Issues & Notes

- Goal files are stored in the current directory
- File names should not contain special characters invalid for your OS
- Completion status is stored as boolean (0 = False, 1 = True)

## Contributing

Feel free to fork this repository and submit pull requests with improvements!

## License

This project is open source and available under the MIT License.

---

**Happy goal tracking! 🎯**
