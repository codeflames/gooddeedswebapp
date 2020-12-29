from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from gooddeeds.auth import login_required
from gooddeeds.db import get_db

bp = Blueprint('gooddeeds', __name__)



@bp.route('/')
def index():
    return render_template('gooddeeds/index.html')


@bp.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    deeds = db.execute(
        "SELECT title, location FROM deeds WHERE userid=:user", {"user":g.user['id']}
    )
    return render_template('gooddeeds/dashboard.html', deeds=deeds)



@bp.route('/createdeed', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        address = request.form['address']

        error = None

        if not title:
            error = 'Title is required.'
        elif not description:
            error = 'description is needed'
        elif not location:
            error = 'location is needed'
        elif not address:
            error = 'address is needed'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO deeds (title, description, location, address, userid)'
                ' VALUES (?, ?, ?, ?, ?)',
                (title, description, location, address, g.user['id'])
            )
            db.commit()
            return redirect(url_for('gooddeeds.dashboard'))

    return render_template('gooddeeds/createdeed.html')



