from flask_smorest import Blueprint
from flask import render_template, request
from flask.views import MethodView
from rescources.generateshort import generate_short
from models import UrlModel
from db import db


shortner = Blueprint('short', __name__, description = "the main app")

@shortner.route('/<short_url>')

def redirect(short_url):
    pass

@shortner.route('/')
def index():
    return render_template('index.html')

@shortner.route('/add_link', methods = ['POST'])
def add_link():
    origin_url = request.form['original_url']
    short_url = generate_short()
    url = UrlModel(original_url = origin_url,short_url = short_url)
    db.session.add(url)
    db.session.commit()

    return url
        
@shortner.route('/stats')
def stats():
    pass