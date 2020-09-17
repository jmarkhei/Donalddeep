from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.SQLAlchemy(APP)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    date_created = 

@APP.route('/')
def index():
    ''' Displays index page accessible at '/' '''
    return render_template('index.html')


if __name__ == '__main__':
    APP.debug = True
    APP.run()
