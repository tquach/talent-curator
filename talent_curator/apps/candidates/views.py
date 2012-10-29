import os
import requests
import json

from flask import redirect, render_template, session, g, url_for, request, flash, Blueprint

from talent_curator import app, _basedir
from talent_curator.apps.google import oauth_client
from talent_curator.decorators import login_required, templated

logger = app.logger

candidates_blueprint = Blueprint('candidates_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates', 'candidates'))


@candidates_blueprint.route('/list')
@login_required
def list():
    return render_template('list.html', candidates=dict())
