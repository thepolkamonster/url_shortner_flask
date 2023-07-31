from db import db
from datetime import datetime
import string
from random import choices

class UrlModel(db.Model):
    __tablename__ = "urls"
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), unique=True, nullable=False)
    short_url = db.Column(db.String(5), unique = True)
    visits = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short()

    def generate_short(self):
        symbols = string.digits + string.ascii_letters
        short_url = ''.join(choices(symbols, k = 3))
    
        link = self.query.filter_by(short_url = short_url).first()

        if link:
            return self.generate_short()
        
        return short_url


