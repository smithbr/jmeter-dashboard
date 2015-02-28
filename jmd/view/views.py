from flask.ext.login import login_user, logout_user
from flask import render_template, request, flash, redirect, url_for

from jmd import app
from jmd.model.forms import SignupForm
from jmd.model.user import UserObj


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('email')
        passwd = request.form.get('password')
        try:
            assert user and passwd, "Username and password are required fields."
        except AssertionError as e:
            flash(e.message, 'danger')
        else:
            user = UserObj.login(user, passwd)
            if user:
                login_user(user)
                flash('Logged in successfully', 'success')
                return redirect(url_for('index'))
            else:
                flash('Unable to verify username and password', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        app.logger.debug('validate')
        email = request.form.get('email')
        passwd = request.form.get('passwd')
        passwd_verify = request.form.get('passwd_verify')
        if passwd == passwd_verify:
            result = UserObj.create(email, passwd)
            app.logger.debug(result)
            if result:
                flash('User account successfully created.')
                return redirect(url_for('index'))
        else:
            flash('Passwords do not match!', 'danger')
    return render_template('signup.html', form=form)
