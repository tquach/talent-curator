import os
from flask import Blueprint, g

from talent_curator import _basedir
from talent_curator.decorators import templated, login_required

profile_blueprint = Blueprint('profile_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates', 'profile'))


@profile_blueprint.route("/")
@templated('/profile/index.html')
@login_required
def index():
    return {'account': g.user}
