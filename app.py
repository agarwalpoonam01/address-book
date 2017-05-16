from flask import Flask, render_template, request, redirect, url_for,\
    session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler
import models
from functools import wraps
import flask_login_auth
from forms import *
import logging


app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
app.config.from_object('config')
db = SQLAlchemy(app)


# Decorator's
def login_requied(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'name' in session:
            return f(*args, **kwargs)
        else:
            flash(' Sorry! You Need to Login to view this page')
            return redirect(url_for('login'))
    return wrap


def logout_requied(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'name' in session:
            flash(
                ' Sorry! You are logged in Already. Logout to Do your Action')
            return redirect(url_for('home'))
        else:
            return f(*args, **kwargs)
    return wrap



@app.route('/register', methods=['GET', 'POST'])
@login_requied
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        user = models.create_user(
            form.firstname.data, form.lastname.data, form.group.data,
            form.email.data,form.address.data,form.phonenumber.data, 
        )
        if user == 1:
            flash(
                'ERROR! Please enter something or check yours\
                username or user already exists'
            )
            return redirect(url_for('register'))
        else:
            return redirect(url_for('home'))
    return render_template('forms/register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@login_requied
def home():
    messages = models.message_show()
    #redirect(url_for('login'))
    return render_template('pages/placeholder.home.html', messages=messages, session=session) # noqa


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/logout')
@login_requied
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
@logout_requied
def login():
    error = None
    session.clear()
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = form.name.data
        password = form.password.data
        value = flask_login_auth.authenticate(username, password)
        print(value);
        print(" line 112");
        if (value == 1):

            session['name'] = username
            messages = models.message_show()
            return redirect(url_for('register'))
        else:
            error = 'Invalid username or password \
            Please try again!'
            return render_template('forms/login.html', form=form, error=error)
    return render_template('forms/login.html', form=form)


@app.route('/search_lastname', methods=['GET', 'POST'])
@login_requied
def search_lastname():
    form = SearchForm(request.form)
    if request.method == 'POST':
        match = models.search(
            form.search4.data, form.value.data
        )
        search = form.search4.data
        return render_template('pages/placeholder.search.html', search=search,
                           match=match)
    return render_template('forms/search_lastname.html', form=form)


@app.route('/search_firstname_lastname', methods=['GET', 'POST'])
@login_requied
def search_firstname_lastname():
    form = SearchForm(request.form)
    if request.method == 'POST':
        match = models.search(
            form.search5.data, form.value.data, form.value2.data
        )
        search = form.search5.data
        return render_template('pages/placeholder.search.html', search=search,
                           match=match)
    return render_template('forms/search_firstname_lastname.html', form=form)

@app.route('/search_firstname', methods=['GET', 'POST'])
@login_requied
def search_firstname():
    form = SearchForm(request.form)
    if request.method == 'POST':
        match = models.search(
            form.search3.data, form.value.data
        )
        search = form.search3.data
        return render_template('pages/placeholder.search.html', search=search,
                           match=match)
    return render_template('forms/search_firstname.html', form=form)

@app.route('/search_group', methods=['GET', 'POST'])
@login_requied
def search_group():
    form = SearchForm(request.form)
    if request.method == 'POST':
        match = models.search(
            form.search.data, form.value.data
        )
        search = form.search.data
        return render_template('pages/placeholder.search.html', search=search,
                           match=match)
    return render_template('forms/search_group.html', form=form)

@app.route('/search_person', methods=['GET', 'POST'])
@login_requied
def search_person():
    form = SearchForm(request.form)
    if request.method == 'POST':
        match = models.search(
            form.search2.data, form.value.data, form.value2.data
        )
        search = form.search2.data
        return render_template('pages/placeholder.search.html', search=search,
                           match=match)
    return render_template('forms/search_person.html', form=form)

@app.route('/add_group', methods=['GET', 'POST'])
@login_requied
def add_group():
    form = AddGroupForm(request.form)
    if request.method == 'POST':
        group = models.add_group(
            form.value.data
        )
        if group == 1:
            flash(
                'ERROR! Please enter something or check yours\
                group already exists'
            )
            return redirect(url_for('add_group'))
        else:
            return redirect(url_for('home'))
    return render_template('forms/add_group.html', form=form)

@app.route('/index')
@login_requied
def index():
    project = flask_login_auth.show_project(session['usersid'])
    session['project'] = project
    return render_template('pages/placeholder.home.html', session=session)


@app.route('/addgroup')
@login_requied
def indexs():
    project = flask_login_auth.show_project(session['usersid'])
    session['project'] = project
    return render_template('pages/placeholder.home.html', session=session)



# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('% (asctime)s % (levelname)s: % (message)s\
                  [in % (pathname)s: % (lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


# Default port:
if __name__ == '__main__':
    app.run(debug=True)
