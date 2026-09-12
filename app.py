from flask import Flask

app = Flask(__name__)


tasks = [
    {
        "id": 1,
        "title": "Learn Git",
        "completed": False,
    },
    {
        "id": 2,
        "title": "Create first pull request",
        "completed": False,
    },
]


@app.route("/")
def home():
    return {"message": "Task Manager API is running"}


@app.route("/tasks")
def get_tasks():
    return {"tasks": tasks}


if __name__ == "__main__":
    app.run(debug=True)