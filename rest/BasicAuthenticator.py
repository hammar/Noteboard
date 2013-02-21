import rest

from auth import checkAuthorization

from google.appengine.api import users

class BasicAuthenticator(rest.Authenticator):
    """Example implementation of HTTP Basic Auth."""

    def __init__(self):
        super(BasicAuthenticator, self).__init__()

    def authenticate(self, dispatcher):
		if users.is_current_user_admin() or checkAuthorization():
			return
		else:
			dispatcher.forbidden()