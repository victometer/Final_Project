from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository


sessions_blueprint = Blueprint('sessions', __name__)

@sessions_blueprint.route('/sessions')
def show_all_sessions():
    all_sessions = session_repository.select_all()
    return render_template('sessions/index.html', all_sessions = all_sessions)
