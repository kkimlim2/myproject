from flask import Blueprint, render_template
from pybo.models import Review
bp = Blueprint('review', __name__, url_prefix='/review')

@bp.route('/<string:musical>/')
def menu(musical):
    temp = Review.query.filter(Review.title == musical).all()
    casting = [t.actors for t in temp]
    return render_template("review.html", title=musical, casting=casting)

@bp.route('/<string:musical>/<string:casting>')
def review(musical, casting):
    temp = Review.query.filter(Review.title == musical).all()
    casting = [t.actors for t in temp]
    temp = Review.query.filter((Review.title == musical) and (Review.actors == casting)).all()
    content = temp[0].content.split('\n')
    actors = temp[0].actors.split(',')
    roles = temp[0].roles.split(',')
    info = [roles[i]+": "+actors[i] for i in range(len(actors))]
    return render_template("review_.html", title=musical, casting=casting, content=content, info=info)


