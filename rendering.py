import jinja2
import os

from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

def renderTemplate(template_name,template_values):
	"""Wrapper function for rendering a template including a logout URL."""
	if template_values == None:
		template_values = {}
	template = jinja_environment.get_template(template_name)
	template_values['logout_url'] = users.create_logout_url("/")
	template_values['user_name'] = users.get_current_user().nickname()
	return template.render(template_values)