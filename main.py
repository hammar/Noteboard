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

from auth import requiresLogin
from errors import *
from rendering import renderTemplate
from models import Note
from rest.BasicAuthenticator import BasicAuthenticator
import rest

class Index(webapp2.RequestHandler):
	@requiresLogin
	def get(self):
		allNotes = Note.all().order("-text")
		template_values = {
			'notes': allNotes
		}
		self.response.write(renderTemplate('index.html',template_values))

app = webapp2.WSGIApplication([
    ('/', Index),
	('/rest/.*', rest.Dispatcher)
], debug=True)
app.error_handlers[403] = handle_403

rest.Dispatcher.authenticator = BasicAuthenticator()
rest.Dispatcher.base_url = "/rest"
rest.Dispatcher.add_models({
  "note": Note})
