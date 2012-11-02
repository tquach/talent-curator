import os
from flask import Blueprint, g, jsonify

from talent_curator import _basedir
from talent_curator.apps.profile import models
from talent_curator.decorators import templated, login_required

profile_blueprint = Blueprint('profile_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates', 'profile'))


@profile_blueprint.route("/")
@templated('/profile/index.html')
@login_required
def index():
    return {'account': g.user}


@profile_blueprint.route("/show/<int:profile_id>")
@login_required
def json_profile(profile_id):
    user = models.User.query.get(profile_id)
    if user:
        return jsonify(firstName=user.first_name, lastName=user.last_name, email=user.email)
    else:
        return jsonify(result='error.notFound')
