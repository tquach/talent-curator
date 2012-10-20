# import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('talent_curator.settings.local')

import talent_curator.views
