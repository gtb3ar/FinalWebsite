from flask import Flask, render_template, request, redirect, url_for, Blueprint
from . import db
from .models import Todo

view = Blueprint("view", __name__)

@view.route("/")
def home():
    todo_list = Todo.query.all()
    message = request.args.get('message', None)
    return render_template("index.html", todo_list=todo_list, message=message)

@view.route('/add', methods=['POST'])
def add():
    try:
        task = request.form.get('task')
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('view.home'))
    except:
        return redirect(url_for('view.home', message="Failed to append task!"))


@view.route('/update/<todo_id>')
def update(todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        db.session.commit()
        return redirect(url_for('view.home'))
    except:
        return redirect(url_for('view.home', message="Failed to update task!"))

@view.route('/delete/<todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('view.home'))