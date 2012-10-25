from flask import redirect, session, g, url_for, request, flash, render_template, Blueprint

from talent_curator import app, _basedir

from talent_curator.decorators import login_required, templated
from talent_curator.database import db_session

from talent_curator.apps.google import oauth_client, api
from talent_curator.apps.profile import models

import os
import requests

REDIRECT_URI = '/oauth2callback'

GOOGLE_USER_INFO = 'https://www.googleapis.com/oauth2/v1/userinfo'
GOOGLE_ACCESS_TOKEN = 'access_token'

logger = app.logger

google_drive = api.GoogleDriveClient(oauth_client)

main_blueprint = Blueprint('main_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates'))


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/login')
def login():
    logger.debug('Login initiated.')
    callback = url_for('main_blueprint.oauth_authorized', _external=True)
    logger.debug("Callback %s", callback)
    return oauth_client.authorize(callback=callback)


@oauth_client.tokengetter
def get_google_token(token=None):
    return session.get(GOOGLE_ACCESS_TOKEN)


@main_blueprint.route(REDIRECT_URI)
@oauth_client.authorized_handler
def oauth_authorized(resp):
    logger.debug('Received resp %s ', resp)

    if resp is not None:
        access_token = resp[GOOGLE_ACCESS_TOKEN]
        session[GOOGLE_ACCESS_TOKEN] = access_token, ''

        logger.debug('Access_token=' + access_token)
        headers = {'Authorization': 'OAuth ' + access_token}
        r = requests.get(GOOGLE_USER_INFO, headers=headers)
        logger.debug("Received response %s", r.json)
        email_address = r.json['email']
        user = models.User.query.filter_by(email=email_address).first()

        if user is None:
            user = models.User(email=email_address, name=r.json['name'],
                first_name=r.json['given_name'], last_name=r.json['family_name'])
            db_session.add(user)
            db_session.commit()

        session['user_id'] = user.id

        g.user = user
        logger.debug('User is loaded %s', user)
    else:
        logger.debug(request.args)
        if request.args and request.args['error']:
            flash('Access Denied: Please grant permission to access your Google Account.')

    return redirect(url_for('main_blueprint.index'))


@main_blueprint.route('/logout')
def logout():
    session[GOOGLE_ACCESS_TOKEN] = None
    session['user_id'] = 0
    g.user = None
    return redirect(url_for('main_blueprint.index'))


@main_blueprint.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        logger.debug('Loading user with id %s', session['user_id'])
        g.user = models.User.query.get(session['user_id'])
        logger.debug("Adding user to g %s", g.user)


@main_blueprint.route('/candidates')
@login_required
@templated('/candidates/list.html')
def candidates():
    access_token = session[GOOGLE_ACCESS_TOKEN]
    if access_token is not None:
        access_token = access_token[0]
        #data = {'key': 'AIzaSyDfsJHHBvU0Fc6eJCGH9J0cGXepOkJiBUw'}
        data = {}
        headers = {'Authorization': 'Bearer ' + access_token}
        r = requests.get('https://www.googleapis.com/drive/v2/files/0B57Vt7WtXq-beU5rbERaSDJ3dGc', params=data, headers=headers)
        logger.debug("API request %s", r.request.headers)
        logger.debug("API request %s", r.request.full_url)
        logger.debug("API response %s", r.content)
    return None
