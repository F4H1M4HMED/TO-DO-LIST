from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will store your tasks
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('content')
        if task_content:
            tasks.append(task_content)
            return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/move_up/<int:task_id>')
def move_up(task_id):
    if 1 <= task_id < len(tasks):
        tasks[task_id], tasks[task_id - 1] = tasks[task_id - 1], tasks[task_id]
    return redirect(url_for('index'))

@app.route('/move_down/<int:task_id>')
def move_down(task_id):
    if 0 <= task_id < len(tasks) - 1:
        tasks[task_id], tasks[task_id + 1] = tasks[task_id + 1], tasks[task_id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)