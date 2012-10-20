from urllib2 import Request, urlopen, URLError

from flask import redirect, render_template, session, g, url_for
from talent_curator import app, main_blueprint
from flask_oauth import OAuth

import json


GOOGLE_CLIENT_ID = '836771404345.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'SkXinXi8AwK26BWOLOQZ8yd3'
GOOGLE_ACCESS_TOKEN = 'access_token'
REDIRECT_URI = '/oauth2callback'

logger = app.logger

oauth = OAuth()
google = oauth.remote_app('talent_curator',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email \
             https://www.googleapis.com/auth/userinfo.profile',
        'response_type': 'code',
        'state': 'random_nonce_123'
    },
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_secret=GOOGLE_CLIENT_SECRET,
    consumer_key=GOOGLE_CLIENT_ID)


@google.tokengetter
def get_google_token(token=None):
    logger.debug("Getting token %s", token)
    return session.get(GOOGLE_ACCESS_TOKEN)


@main_blueprint.route('/')
def index():
    access_token = session.get(GOOGLE_ACCESS_TOKEN)
    if access_token is not None:
        access_token = access_token[0]
        logger.debug('Access_token=' + access_token)
        headers = {'Authorization': 'OAuth ' + access_token}
        req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                        None, headers)

        try:
            res = urlopen(req)
        except URLError, e:
            if e.code == 401:
                # Unauthorized
                session.pop(GOOGLE_ACCESS_TOKEN, None)
                return redirect(url_for('main_blueprint.index'))
            return res.read()

        g.user = json.loads(res.read())
        logger.debug("Authorization received from %s", g.user)
    return render_template('index.html')


@main_blueprint.route('/login')
def login():
    logger.debug('Login initiated.')
    callback = url_for('main_blueprint.oauth_authorized', _external=True)
    logger.debug("Callback %s", callback)
    return google.authorize(callback=callback)


@main_blueprint.route(REDIRECT_URI)
@google.authorized_handler
def oauth_authorized(resp):
    logger.debug('Received resp %s ', resp)
    access_token = resp[GOOGLE_ACCESS_TOKEN]
    session[GOOGLE_ACCESS_TOKEN] = access_token, ''
    return redirect(url_for('main_blueprint.index'))


@main_blueprint.route('/logout')
def logout():
    session[GOOGLE_ACCESS_TOKEN] = None
    g.user = None
    return redirect(url_for('main_blueprint.index'))
