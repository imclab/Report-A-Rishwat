from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, request, \
                  session, g, redirect, \
                  url_for, abort, render_template, flash
import time
import random
import string

# configuration
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
    return render_template('index.html')

@app.route('/list')
def mainpage():
    return render_template('list.html')

@app.route('/categories')
def mainpage():
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
    curtime = time.localtime()
    PetitionID = random.randint(1,100000)
    entrytime = "%d/%d,%d" % (curtime.tm_mon, 
                              curtime.tm_mday, 
                              curtime.tm_year)
    g.db.execute('insert into petitions (PID, ' + \
                 'AccusName, Crime, Location, ' + \
                 'DateOfCrime, DateOfPetition, ' + \
                 'Addinfo, BribePaid) ' + \
                 'values (?,?,?,?,?,?,?,?)',
                 [PetitionID, 
                  request.form['officer'], 
                  request.form['service'], 
                  request.form['location'], 
                  request.form['date'], 
                  entrytime, 
                  request.form['description'],
                  int(request.form['amount'])])
    g.db.commit()
    return render_template('Thankyou.html')

if __name__ == '__main__':
    app.run()
