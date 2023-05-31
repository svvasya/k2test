from flask import render_template, redirect, request
from flask_login import login_user, current_user,  logout_user, login_required
from k2root.config import app
from flask import Blueprint

k2test_bp = Blueprint('k2test', __name__)

@k2test_bp.route('/new')
def new_component():
    return 'нова встановлена компонента'
