from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks
todos = []

@app.route('/')
def index():
    return render_template('todolist.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        todos.append({'task': task, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:index>')
def complete_task(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/remove/<int:index>')
def remove_task(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
