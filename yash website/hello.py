import flask

application = app = flask.Flask(__name__)
# available_themes =  ['CERULEAN', 'COSMO', 'CYBORG', 'DARKLY', 'FLATLY', 'JOURNAL', 
#                       'LITERA', 'LUMEN', 'LUX', 'MATERIA', 'MINTY', 'PULSE', 'SANDSTONE', 
#                       'SIMPLEX', 'SKETCHY', 'SLATE', 'SOLAR', 'SPACELAB', 'SUPERHERO', 'UNITED', 'YETI'
#                       ]

themes=['united','amelia','slate','flatly','default']
theme=themes[4]

@app.route('/')
def yash():
	return flask.render_template('hello.html',theme=theme)


@app.route('/info')
def info():
	return flask.render_template('yash.html',theme=theme)


app.run(debug=True)