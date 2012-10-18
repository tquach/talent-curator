# import os
from flask import Flask
from talent_curator.database import init_db, db_session

app = Flask(__name__)
app.config.from_object('talent_curator.settings.local')

import talent_curator.views

init_db()

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

