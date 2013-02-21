from rendering import renderTemplate

def handle_403(request, response, exception):
	response.write(renderTemplate('403.html',None))