from flask import render_template, redirect, request
from flask_login import login_user, current_user,  logout_user, login_required

@app.route('/new')
@login_required
def new_components():
    return 'нова встановлена компонента'