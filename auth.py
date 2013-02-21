import webapp2

from google.appengine.ext import db
from google.appengine.api import users

from models import UserPreferences

def checkAuthorization():
	userEmail = users.get_current_user().email()
	userKey = db.Key.from_path('UserPreferences',userEmail)
	if db.get(userKey) == None:
		return False
	else:
		return True

def requiresLogin(fun):
	def decorate(requestHandler):
		if users.is_current_user_admin() or checkAuthorization():
			fun(requestHandler)
		else:
			raise webapp2.abort(403)
	return decorate