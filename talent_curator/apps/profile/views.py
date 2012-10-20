from flask import render_template
from talent_curator import app, profile_blueprint


@profile_blueprint.route("/")
def manage_account():
    return render_template('account.html')
