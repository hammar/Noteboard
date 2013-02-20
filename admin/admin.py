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
import os

import webapp2

from google.appengine.api import users
from google.appengine.ext.webapp import template

class Index(webapp2.RequestHandler):
    def get(self):
		template_values = {
			'users': ['karl@karlhammar.com','nisse@nisse.com']
		}
		self.response.write(renderTemplate('index.html',template_values))

def renderTemplate(template_name,template_values):
	"""Wrapper function for rendering a template including a logout URL."""
	path = os.path.join(os.path.dirname(__file__), template_name)
	template_values['logout_url'] = users.create_logout_url("/")
	return template.render(path, template_values)

app = webapp2.WSGIApplication([
    ('/admin/', Index)
], debug=True)
