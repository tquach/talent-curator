from flask import session, g

from talent_curator import app
from talent_curator.apps.profile import models


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        app.logger.debug('Loading user with id %s', session['user_id'])
        g.user = models.User.query.get(session['user_id'])
        app.logger.debug("Adding user to g %s", g.user)
