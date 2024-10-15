
# To-Do List Web Application

A simple To-Do List app built using Python and Flask. Manage your tasks by adding, completing, and removing them.

## Features
- Add tasks to the to-do list.
- Mark tasks as complete.
- Remove tasks from the list.

## Requirements
- Python 3.x
- Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todolist-flask.git
   cd todolist-flask
   ```

2. Set up a virtual environment (optional):
   ```bash
   python -m venv venv
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the app:
   ```bash
   python app.py
   ```

Visit `http://127.0.0.1:5000/` in your browser to access the To-Do List.

## File Structure
```
todolist-flask/
│
├── app.py               # Main Flask app
├── templates/           # HTML templates
│   └── todolist.html     # To-Do list template
└── README.md            # This file
```

## Usage
- **Add Task**: Go to `http://127.0.0.1:5000/add/YourTaskName`
- **Complete Task**: Click the "Complete" link next to a task.
- **Remove Task**: Click the "Remove" link next to a task.

## License
MIT License.

