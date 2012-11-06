import os

from flask import render_template, session, Blueprint, json, request, flash

from talent_curator import app, _basedir
from talent_curator.apps.google import drive
from talent_curator.decorators import login_required

logger = app.logger

google_api = drive.GoogleDriveAPI()

candidates_blueprint = Blueprint('candidates_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates', 'candidates'))


@candidates_blueprint.route('/children')
@login_required
def children():
    access_token = session['access_token']
    access_token = access_token[0]
    logger.info('Searching for documents: %s' % request.args)
    results = google_api.children(access_token, request.args['folder_id'])
    children = []
    for result in results:
        file_resource = google_api.get_document(access_token, result['id'])
        children.append(file_resource)
    return render_template('list.html', children=children)


@candidates_blueprint.route('/list')
@login_required
def list():
    access_token = session['access_token']
    access_token = access_token[0]
    logger.info('Searching for documents: %s' % request.args)
    results = google_api.search(access_token, 'title="Candidate CVs"')
    return render_template('list.html', results=results, raw_json=json.dumps(results[0], indent=4))


@candidates_blueprint.route('/show')
@login_required
def show():
    doc_id = request.args['document_id'] or request.form.get('document_id')
    if doc_id:
        access_token = session['access_token']
        access_token = access_token[0]
        logger.info(access_token)
        file_resource = google_api.get_document(access_token, doc_id)
        if file_resource:
            return render_template('show.html', document=file_resource, raw=json.dumps(file_resource, indent=4))
        else:
            flash('No document found for the given Doc ID.')
            return render_template('show.html')
    else:
        return render_template('show.html')
