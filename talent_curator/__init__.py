import os
from flask import Flask

_basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object('talent_curator.settings.local')

from talent_curator.apps.core.views import main_blueprint
app.register_blueprint(main_blueprint)

from talent_curator.apps.profile.views import profile_blueprint
app.register_blueprint(profile_blueprint, url_prefix="/account")
