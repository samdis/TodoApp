
from flask import render_template, redirect, request
from todo import app
from todo.api import create_task, get_tasks, delete_task, finish_task

"""URLs for our application."""


@app.route("/")
def task_list():
    tasks = get_tasks()
    return render_template("application.html", tasks=tasks)


@app.route("/task", methods=["POST"])
def task_create():
    body = request.form["body"]
    create_task(body)
    return redirect("/")


@app.route("/delete/<int:task_id>")
def task_delete(task_id):
    delete_task(task_id)
    return redirect("/")


@app.route("/done/<int:task_id>")
def task_done(task_id):
    finish_task(task_id)
    return redirect("/")
