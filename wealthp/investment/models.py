from sqlalchemy import Column

from ..extensions import db


class Investment(db.Model):

    __tablename__ = 'users'

    id = Column(db.Unicode(16), primary_key=True)
    name = Column(db.String(256), nullable=False, unique=True)
    amount = Column(db.Integer, nullable=False, default=0)
    course_buy = Column(db.Float, nullable=False)       # TODO: history data with other table
    currency = Column(db.Integer, nullable=False, default='CHF')

    def update_course(self):
        pass

    @property
    def value(self):
        return self.amount * self.course_buy
