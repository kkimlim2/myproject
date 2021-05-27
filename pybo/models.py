from pybo import db
## db.realtionship, db.ForeignKey, db.backref

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # actors, rolse 다 () 이렇게 세트로 묶어서 입력할 것
    actors = db.Column(db.Text(), nullable=False)
    roles = db.Column(db.Text(), nullable=False)
    # (극장, 좌석)이 세트로 묶어서 입력할 것
    seat = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.String(16), nullable=False)


#나중에 seat를 db.relationship으로 바꿔야 할지도 모르겠으나 그냥 패스
class View(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theater = db.Column(db.String(50), nullable=False)
    seat = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text(), nullable=False)


