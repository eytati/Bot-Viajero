from oauth2client.client import flow_from_clientsecrets
'''
from requests.auth import HTTPBasicAuth



requests.get('https://api.github.com/user', auth=('user', 'pass'))


url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)

'''

low = flow_from_clientsecrets('path_to_directory/client_secrets.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://example.com/auth_return')