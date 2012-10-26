import os
import requests

from flask import redirect, render_template, session, g, url_for, request, flash, Blueprint

from talent_curator import _basedir
from talent_curator.apps.google import oauth_client, api

candidates_blueprint = Blueprint('candidates_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates', 'candidates'))


@candidates_blueprint.route('/list')
def list():

    return render_template('list.html', candidates=[])
