# import os
from flask import Flask, Blueprint

app = Flask(__name__)
app.config.from_object('talent_curator.settings.local')

# Register blueprints
profile_blueprint = Blueprint('profile_blueprint', __name__,
                        template_folder='templates/profile')

main_blueprint = Blueprint('main_blueprint', __name__,
                        template_folder='templates')

# Import routes
import talent_curator.apps.core.views
import talent_curator.apps.profile.views

app.register_blueprint(main_blueprint)
app.register_blueprint(profile_blueprint, url_prefix="/account")