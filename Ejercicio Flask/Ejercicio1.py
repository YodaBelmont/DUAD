from flask import Flask, request
import json

app = Flask(__name__)

task_state = ["pending", "in progress", "completed"]


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)



@app.route("/tasks")
def show_tasks():
    task_list = load_tasks()
    filtered_tasks = []

    task_filter = request.args.get("state")

    if task_filter:
        for task in task_list:
            if task_filter == task["state"]:
                filtered_tasks.append(task)
    else:
        return task_list
    return filtered_tasks


@app.route("/tasks", methods=["POST"])
def create_task():
    task_list = load_tasks()
    data = request.json
    if "id" not in data:
        return {"error": "id not found"}, 400

    for task in task_list:
        if task["id"] == data["id"]:
            return{"error":"there already is a task registered with that id"}, 409

    if "title" not in data:
        return {"error": "title not found"}, 400

    if "description" not in data:
        return {"error": "description not found"}, 400

    if "state" not in data:
        return {"error": "state not found"}, 400

    if data["state"] not in task_state:
        return{"error": "state value was not valid / must use 'pending', 'in progress' or 'completed'"}, 400
    
    task_list.append(data)

    save_tasks(task_list)

    return {"task added":data}, 201


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task_list = load_tasks()
    for task in task_list:
        if task["id"] == id:
            task_list.remove(task)
            save_tasks(task_list)
            return {"message":"task deleted"}
    return {"message":"task not found"}, 404 


@app.route("/tasks/<int:id>", methods=["PATCH"])
def edit_task(id):
    task_list = load_tasks()
    data = request.json

    allowed_fields = ["title", "description", "state"]

    for task in task_list:
        if task["id"] == id:

            for key, value in data.items():
                if key not in allowed_fields:
                    return {"error": f"field '{key}' cannot be modified"}, 400

                if key == "state" and value not in task_state:
                    return {"error": "invalid state"}, 400

            task.update(data)

            save_tasks(task_list)

            return {"message": "task modified successfully"}

    return {"error": "task not found"}, 404


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
