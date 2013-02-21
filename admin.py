#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from google.appengine.api import users

from google.appengine.ext import db

from models import UserPreferences
from rendering import renderTemplate

class AddUser(webapp2.RequestHandler):
	def post(self):
		email = self.request.get('email')
		name = self.request.get('name')
		newUser = UserPreferences(key_name=email, email=email, name=name)
		newUser.put()
		self.redirect("/admin/")

class DeleteUser(webapp2.RequestHandler):
	def get(self):
		email = self.request.get('email')
		user = UserPreferences.gql("WHERE email = :1", email).get()
		user.delete()
		self.redirect("/admin/")

class Index(webapp2.RequestHandler):
    def get(self):
		allUsers = UserPreferences.all().order("-name")
		template_values = {
			'users': allUsers
		}
		self.response.write(renderTemplate('admin.html',template_values))

app = webapp2.WSGIApplication([
    ('/admin/', Index),
    ('/admin/addUser', AddUser),
    ('/admin/deleteUser', DeleteUser)
], debug=True)
