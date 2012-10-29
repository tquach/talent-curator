from flask import session, g

from talent_curator import app
from talent_curator.apps.profile import models


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = models.User.query.get(session['user_id'])
