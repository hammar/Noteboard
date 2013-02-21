from google.appengine.ext import db

class UserPreferences(db.Model):
	email = db.StringProperty()
	name = db.StringProperty()