from flask import Flask

from services.task_service import get_all_tasks

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Task Manager API is running"}


@app.route("/tasks")
def get_tasks():
    return {"tasks": get_all_tasks()}


if __name__ == "__main__":
    app.run(debug=True)