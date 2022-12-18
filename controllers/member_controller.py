from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository


members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def show_all_members():
    members = member_repository.select_all()
    return render_template('members/index.html', members = members)

@members_blueprint.route('/members/<id>')
def show(id):
    member = member_repository.select(id)
    gym_classes = gym_class_repository.gym_classes_for_member(member)
    return render_template('members/show.html', member = member, gym_classes = gym_classes)

@members_blueprint.route('/members/new')
def new_member_click():
    return render_template('/members/new.html')

@members_blueprint.route('/members/new', methods = ["POST"])
def create_new_member():
    name = request.form['name']
    new_member = Member(name)
    member_repository.save(new_member)
    return redirect('/members/')

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    member = Member(name, id)
    member_repository.update(member)
    return redirect("/members")
