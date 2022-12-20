from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
from models.member import  Member
from models.session import  Session
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository


gym_classes_blueprint = Blueprint('gym_classes', __name__)

@gym_classes_blueprint.route('/gym_classes')
def show_all_classes():
    all_classes = gym_class_repository.select_all()
    return render_template('gym_classes/index.html', gym_classes = all_classes)


@gym_classes_blueprint.route('/gym_classes/<id>')
def show(id):
    gym_class = gym_class_repository.select(id)
    members = member_repository.members_for_gym_class(gym_class)
    return render_template('gym_classes/show.html', gym_class = gym_class, members = members)


@gym_classes_blueprint.route('/gym_classes/new')
def click_new_class():
    return render_template('gym_classes/new.html')


@gym_classes_blueprint.route('/gym_classes/new', methods = ["POST"])
def create_new_class():
    name = request.form['name']
    time = request.form['time']
    duration = request.form['duration']
    capacity = request.fotm['capacity']
    new_class = Gym_class(name, time, duration, capacity)
    gym_class_repository.save(new_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('gym_classes/edit.html', gym_class=gym_class)

@gym_classes_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_gym_class(id):
    name = request.form["name"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form['capacity']
    gym_class = Gym_class(name, time, duration, capacity, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")

@gym_classes_blueprint.route('/gym_classes/<id>/book')
def book_class(id):
    gym_class = gym_class_repository.select(id)
    members = member_repository.select_all()
    return render_template('gym_classes/book.html', error = False, gym_class=gym_class, members=members)


@gym_classes_blueprint.route('/gym_classes/<id>/book', methods = ['POST'])
def show_updated_class(id):

    gym_class = gym_class_repository.select(id)
    members = member_repository.members_for_gym_class(gym_class)
    if gym_class.capacity > len(members):
        member_id = request.form["member-id"]
        member = member_repository.select(member_id)
        session = Session(member, gym_class)
        session_repository.save(session)
    else: 
        return render_template('gym_classes/book.html', error = True, gym_class=gym_class, members=members)
    return redirect('/gym_classes/'+ id)
