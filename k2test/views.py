from flask import render_template, redirect, request
from flask_login import login_user, current_user,  logout_user, login_required
from main import app
from flask import Blueprint

k2test_bp = Blueprint('k2test', __name__)

@k2test_bp.route('/new')
def new_component():
    app = current_app

    
    with app.app_context():
        connection = db.engine.connect()
        query = "SELECT * FROM k2users"
        result = connection.execute(query)
        k2users = result.fetchall()

   
    return k2users
    
    
