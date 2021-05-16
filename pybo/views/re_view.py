from flask import Blueprint, render_template, url_for

bp = Blueprint('review', __name__, url_prefix='/review')
@bp.route('/<string:musical>/')
def review(musical):
    return "hi"