tasks = [
    {
        "id": 1,
        "title": "Learn Git",
        "completed": False
    },
    {
        "id": 2,
        "title": "Create first pull request",
        "completed": False
    }
]


def get_all_tasks():
    return tasks


def create_task(title):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)

    return new_task