from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from uuid import uuid4
import os

app = Flask('__name__', template_folder=os.path.dirname(os.path.realpath(__file__))+'/templates/')
app.config['SECRET_KEY'] = str(uuid4())
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8000, debug = True)