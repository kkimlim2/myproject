from flask import Blueprint, render_template,request,url_for
from werkzeug.utils import redirect

from pybo.models import Review
from pybo import db

from datetime import datetime

bp = Blueprint('write', __name__, url_prefix='/write')

@bp.route('/')
def write():
    return render_template('write.html')

@bp.route('/submit',methods=['POST'])
def submit():
    print(request)
    title = request.form.get('title')
    actor = request.form.get('actor')
    role = request.form.get('role')
    seat = request.form.get('seat')
    content = request.form.get('content')
    date = request.form.get('date')
    review =Review(title=title, actors=actor, roles=role, seat=seat, content=content, create_date=date)
    db.session.add(review)
    db.session.commit()
    return redirect(url_for('main.index'))

