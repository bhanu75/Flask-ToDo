from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import uuid
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# In-memory storage
TASKS = []

@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    details = request.form.get('details')
    deadline = request.form.get('deadline')
    if title:
        TASKS.append({
            'id': str(uuid.uuid4()),
            'title': title,
            'details': details,
            'deadline': deadline,
            'created': datetime.now()
        })
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete(task_id):
    global TASKS
    TASKS = [task for task in TASKS if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    TASKS.clear()
    return redirect(url_for('index'))

@app.route('/task/<task_id>')
def view(task_id):
    task = next((task for task in TASKS if task['id'] == task_id), None)
    if task:
        return render_template('detail.html', task=task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
