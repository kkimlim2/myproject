from flask import Blueprint, render_template, url_for
from pybo.models import Review, View
from werkzeug.utils import redirect
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    #seat: (극장, 좌석정보) => , 기준으로 split
    #극장, 제목의 중복 제거
    theater_list = Review.query.with_entities(Review.seat).all()
    theater_list = [seat[0].split(',')[0] for seat in theater_list]
    theater_list = list(set(theater_list))
    title_list = Review.query.with_entities(Review.title).all()
    title_list = [title[0] for title in title_list]
    title_list = list(set(title_list))

    option = {}
    for name in title_list:
        temp = Review.query.filter(Review.title == name).all()
        a = []
        for t in temp:
            a.append(t.actors)
        option[name] = a

    return render_template('index.html', theater_list=theater_list, title_list=title_list, option=option)

