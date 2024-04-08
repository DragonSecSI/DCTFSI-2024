
from flask import Flask, render_template, request, jsonify
from flask_restful import Api
import os 

app = Flask(__name__)
api = Api(app)

# Sample initial task list
task_list = ["Task 1", "Task 2", "Task 3"]

@app.route('/', methods=['GET', 'POST'])
def task_list_page():
    if request.method == 'POST':
        # Update task list
        global task_list
        print(request.json.get('task_list'))
        if request.json.get('user') == 'admin':
            return jsonify({'message': 'Task list updates successfully, don\'t forget your free flag admin: '+os.environ.get('FLAG'), 'task_list': task_list}), 200
        return jsonify({'message': 'Task list updated successfully!', 'task_list': task_list}), 200
    
    elif request.method == 'GET':
        return render_template('index.html', task_list=task_list)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=False,
    )

