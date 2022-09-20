import os
from flask import Flask, \
    abort as _abort, \
    g as _g, \
    current_app as _current_app, \
    redirect as _redirect, \
    request as _request, \
    session as _session, \
    render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
app = Flask('renovatr')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') ## mysql://username:password@hostname/database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context(*args, **kwargs):
    return dict(db=db) #User=User, all models

@app.route('/')
def index():
    return '<p>{}</p>'.format('erin')

if __name__ == '__main__':
    # app_ctx = app.app_context()
    # app_ctx.push()
    app.run(debug=True)

