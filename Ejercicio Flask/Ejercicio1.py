from flask import Flask, request
import json

app = Flask(__name__)

task_state = ["pending", "in progress", "completed"]
# keys = ["id", "title", "description", "state"]

task_list = []



@app.route("/")
def root():
    with open("tasks.json", "w", encoding="utf-8") as file:
        task_list = json.load(file)
    if not task_list:
        return {"error":"no data to show"}
    return task_list


@app.route("/task")
def show_tasks():
    filtered_tasks = []
    
    task_filter = request.args.get("state")
    
    if task_filter:
        for task in task_list:
            if task_filter == task["state"]:
                filtered_tasks.append(task)
    else:
        return task_list
    return filtered_tasks


@app.route("/create", methods=["POST"])
def create_task():
    data = request.json
    if "id" not in data:
        return {"error": "id not found"}
    
    for task in task_list:
        if task["id"] == data["id"]:
            return{"error":"there already is a task registered with that id"}
    
    if "title" not in data:
        return {"error": "title not found"}
    
    if "description" not in data:
        return {"error": "description not found"}
    
    if "state" not in data:
        return {"error": "state not found"}
    
    if data["state"] not in task_state:
        return{"error": "state value was not valid / must use 'pending', 'in progress' or 'completed'"}
    
    task_list.append(data)
    return {"task added":data}


@app.route("/delete", methods=["DELETE"])
def delete_task():
    data = request.json
    
    for index, task in enumerate(task_list):
        if data["id"] == task["id"]:
            task_list.pop(index)
            return{"task deleted":task}
    return{"error":"task not found"}


# @app.route("/edit", methods=["PATCH"])
# def edit_task():
#     data = request.json
    
#     for


# if __name__ == "__main__":
#     app.run(host="localhost", debug=True)

