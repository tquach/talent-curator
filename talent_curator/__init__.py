# import os
from flask import Flask

app = Flask(__name__)
app.config.from_object('talent_curator.settings.local')

import talent_curator.views
from talent_curator.database import init_db, db_session

init_db()

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

