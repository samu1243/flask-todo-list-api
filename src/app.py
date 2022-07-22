from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    data = jsonify(todos)
    return data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    data_decoded = json.loads(request_body)
    todos.append(data_decoded)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.remove(todos[position])
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)



# Termine el ejercicio leyendo el ReadMe, extremadamente buggy. El post y delete dan error de autorizacion en postman