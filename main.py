import flask

TEMPLATES_FOLDER = ''
STATIC_FOLDER = ''



class MainApp(flask.Flask):
	def __init__(self, appName=__name__):
		flask.Flask.__init__(self, appName)

		self.appName = appName
		self.host = '192.168.0.104'
		self.port = 80	

		self.template_folder = TEMPLATES_FOLDER
		self.static_folder = STATIC_FOLDER



if __name__ == '__main__':
	mainApp = MainApp()

	@mainApp.route('/')
	def index():
		return flask.render_template('index.html')

	mainApp.run(
		host=mainApp.host,
		port=mainApp.port,
		debug=True
	) 
else:
	app = MainApp()

	@app.route('/')
	def index():
		return flask.render_template('index.html')
