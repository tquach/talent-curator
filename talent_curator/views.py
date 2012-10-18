from flask import render_template, session, g
from talent_curator import app
from talent_curator.apps import models
from talent_curator.database import db_session

from flask.ext.openid import OpenID

oid = OpenID(app)
openid = ''


@app.before_request
def lookup_current_user():
    g.user = None
    if 'openid' in session:
        g.user = models.User.query.filter_by(userid=openid).first()


@app.route('/')
def index():
    return render_template('index.html')


@app.after_request
def after_request(response):
    db_session.remove()
    return response
