from google.appengine.ext import db

class UserPreferences(db.Model):
	email = db.StringProperty(required=True)
	name = db.StringProperty(required=True)

class Board(db.Model):
	title = db.StringProperty(required=True)

class Note(db.Model):
	text = db.StringProperty(required=True)
	color = db.StringProperty(required=True, choices=set(["red", "orange", "yellow", "green", "white"]))
	board = db.ReferenceProperty(Board)
	xCoord = db.IntegerProperty(required=True)
	yCoord = db.IntegerProperty(required=True)
	