from flask import Flask, request

from services.task_service import get_all_tasks, create_task

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Task Manager API v2 is running"}


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return {"tasks": get_all_tasks()}


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    task = create_task(data["title"])

    return task, 201


if __name__ == "__main__":
    app.run(debug=True)