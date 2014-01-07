from __future__ import with_statement
import sqlite3
from flask import Flask, request, \
    g, render_template

# configuration
from forms.reportRishwat import RegistrationForm

DATABASE = './schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
@app.route('/index')
def root():
    form = RegistrationForm(request.form)
    return render_template('index.html', form=form)

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/results')
def results():
    result = g.db.execute('SELECT count(Location) FROM petitions')
    val = result.fetchone()
    return render_template('results.html')

@app.route('/report')
def mainpage():
    return render_template('report.html')

@app.route('/ThankYou', methods=['POST'])
def add_entry():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        g.db.execute('insert into petitions (' + \
                     'DateOfCrime, AdministrativeUnit, Location, ' + \
                     'AccusName, BribePaid, ' + \
                     'Description) ' + \
                     'values (?,?,?,?,?,?,?,?)',
                     [request.form['date'],
                      request.form['province'],
                      request.form['location'],
                      request.form['officer'],
                      int(request.form['bribe'],
                      request.form['description']
                      )])
        g.db.commit()
        return render_template('Thankyou.html')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
