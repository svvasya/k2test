from flask import render_template, redirect, request
from flask_login import login_user, current_user,  logout_user, login_required
from flask import current_app as k2
from flask import Blueprint, json
from flask_sqlalchemy import SQLAlchemy


k2test_bp = Blueprint('k2test', __name__)

@k2test_bp.route('/new')
def new_component():
    app = k2
    db = k2.extensions['sqlalchemy'].db

    with app.app_context():
        connection = db.engine.connect()
        query = db.text("SELECT email, login FROM k2users")
        result = connection.execute(query)
        rows = [dict(email=row.email, login=row.login) for row in result]


        # Перетворення результату на JSON
        json_result = json.dumps(rows)

        return json_result
        k2users = result.fetchall()

   
    return k2users
    
   
