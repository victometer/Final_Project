from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository


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
    new_class = Gym_class(name, time, duration)
    gym_class_repository.save(new_class)
    return redirect('/gym_classes')

