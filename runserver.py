#import os
from talent_curator import app
from talent_curator.database import init_db

init_db()
app.run()
