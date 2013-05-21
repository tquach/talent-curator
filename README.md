Summary
-------
This is a Flask project that connects to Google Drive using Google's OAUTH 1.0 implementation.

This also demonstrates practical uses of several Flask modules such as:
* Flask-OAuth
* Flask-SQLAlchemy
* Flask-Login

The interaction between Google Drive API  uses the [requests](http://docs.python-requests.org/en/latest/) library once authorisation has been granted.

Implementation Notes
--------------------

The application follows the guidelines from [Flask Patterns for Large Applications](http://flask.pocoo.org/docs/patterns/packages/) using blueprints and decorators. It uses HTML5 Boilerplate and Bootstrap for the basic layout and design.

The project is structured as follows, following a modular-based approach:

    tree -d
    .
    └── talent_curator
        ├── apps
        │   ├── candidates
        │   │   └── tests
        │   ├── core
        │   ├── google
        │   │   └── tests
        │   └── profile
        ├── settings
        ├── static
        │   ├── css
        │   ├── font
        │   ├── img
        │   │   └── icons
        │   ├── js
        │   │   └── vendor
        │   │       └── bootstrap
        │   └── scss
        │       └── bootstrap
        └── templates
            ├── candidates
            └── profile

Running the Application
-----------------------

After cloning, setting up your virtualenv, etc:

    cd talent-curator/talent_curator/static/scss
    compass compile

Run server

    cd talent-curator
    python runserver.py

Point browser to localhost and enjoy.
