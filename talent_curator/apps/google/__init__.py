from flask_oauth import OAuth

GOOGLE_CLIENT_ID = '836771404345.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'SkXinXi8AwK26BWOLOQZ8yd3'

SCOPES = "https://www.googleapis.com/auth/userinfo.email \
            https://www.googleapis.com/auth/userinfo.profile \
            https://www.googleapis.com/auth/drive"


oauth = OAuth()
oauth_client = oauth.remote_app('talent_curator',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={
        'scope': SCOPES,
        'response_type': 'code',
        'state': 'random_nonce_123'
    },
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_secret=GOOGLE_CLIENT_SECRET,
    consumer_key=GOOGLE_CLIENT_ID)
