import os
from talent_curator import _basedir
from flask import render_template, Blueprint

profile_blueprint = Blueprint('profile_blueprint', __name__,
                        template_folder=os.path.join(_basedir, 'templates/profile'))


@profile_blueprint.route("/")
def manage_account():
    return render_template('account.html')
