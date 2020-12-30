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
        "SELECT id, userid, address, description, title, date, location, isdone FROM deeds WHERE  isdone =:bool", { "bool":False}
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
        date = request.form['date']

        error = None

        if not title:
            error = 'Title is required.'
        elif not description:
            error = 'description is needed'
        elif not location:
            error = 'location is needed'
        elif not address:
            error = 'address is needed'
        elif not date:
            error = "date is required"
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO deeds (title, description, location, isdone, address, userid, date)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                (title, description, location, False, address, g.user['id'], date)
            )
            db.commit()
            return redirect(url_for('gooddeeds.dashboard'))

    return render_template('gooddeeds/createdeed.html')



@bp.route('/completed')
@login_required
def completed():
    db = get_db()
    deeds = db.execute(
        "SELECT id, userid, title, location, address, date, description, isdone FROM deeds WHERE isdone =:bool" , {"bool":True}
    )
    return render_template('gooddeeds/completed.html', deeds=deeds)



@bp.route("/isdone/<int:deed_id>")
@login_required
def isdone(deed_id):
    db = get_db()
    deedid = db.execute(
        "SELECT id, isdone FROM deeds WHERE id =:theid",{"theid":deed_id}
    )

    is_done = None
    is_id = None
    for item in deedid:
        is_done = item['isdone']
        is_id = item['id']
    

    db.execute(
        "UPDATE deeds SET isdone = ? WHERE id = ?",
        (not is_done, is_id,)
    )

    db.commit()

    return redirect(url_for('gooddeeds.dashboard'))

@bp.route('/<int:id>/delete')
@login_required
def delete(id):
    db = get_db()
    deedid = db.execute(
        "SELECT id FROM deeds WHERE id =:theid",{"theid":id}
    )
    is_id = None
    for item in deedid:
        is_id = item['id']

    db.execute('DELETE FROM deeds WHERE id = ?', (is_id,))
    db.commit()

    return redirect(url_for('gooddeeds.dashboard'))

@bp.route('/<int:id>/update',methods=('GET', 'POST') )
@login_required
def update(id):
    db = get_db()
    deeds = db.execute(
        "SELECT * FROM deeds WHERE id =:theid",{"theid":id}
    ).fetchone()
    # is_id = None
    # for item in deedid:
    is_id = deeds['id']

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        address = request.form['address']
        date = request.form['date']

        error = None

        if not title:
            error = 'Title is required.'
        elif not description:
            error = 'description is needed'
        elif not location:
            error = 'location is needed'
        elif not address:
            error = 'address is needed'
        elif not date:
            error = 'date is required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE deeds SET title = ?, description = ?, date = ?, location = ?, address = ? WHERE id = ?',
                (title, description, date, location, address, is_id)
            )
            db.commit()
            return redirect(url_for('gooddeeds.dashboard'))
    
    return render_template('gooddeeds/update.html',deeds = deeds)


@bp.route('/<int:id>/details')
@login_required
def details(id):
    db = get_db()
    deeds = db.execute(
        "SELECT * FROM deeds WHERE  id =:ide", { "ide":id}
    )
    return render_template('gooddeeds/details.html', deeds=deeds)

