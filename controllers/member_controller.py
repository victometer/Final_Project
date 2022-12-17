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
