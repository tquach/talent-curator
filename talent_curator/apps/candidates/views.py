import os

from flask import render_template, session, Blueprint, json, request

from talent_curator import app, _basedir
from talent_curator.apps.google import drive
from talent_curator.decorators import login_required

logger = app.logger

google_api = drive.GoogleDriveAPI()

candidates_blueprint = Blueprint('candidates_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates', 'candidates'))


@candidates_blueprint.route('/list')
@login_required
def list():
    return render_template('list.html', documents={})


@candidates_blueprint.route('/show', methods=['POST'])
@login_required
def get_document_cv():
    document_id = request.form.get('document_id')
    access_token = session['access_token']
    access_token = access_token[0]
    logger.info(access_token)

    file_resource, raw_json = google_api.get_document(access_token, document_id)
    return render_template('list.html', document=file_resource, raw=json.dumps(raw_json, indent=4))
