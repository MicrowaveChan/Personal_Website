import csv
from flask import render_template, url_for, flash, redirect, request
from personal_website import app, bcrypt, db
from personal_website.forms import SignupForm, LoginForm, ContactForm
from personal_website.models import User
from flask_login import login_user, current_user, logout_user, login_required

prefix = 'personal_website/'
@app.route('/')
@app.route('/home')
def home():
    with open(prefix + url_for('static', filename='data/skills.csv')) as f:
        skill_list = list(csv.reader(f))[1:]
    return render_template('home.html', skill_list=skill_list)


@app.route('/projects')
def projects():
    with open(prefix + url_for('static', filename='data/projects.csv')) as f:
        project_list = list(csv.reader(f))[1:]
    return render_template('projects.html', active_page='projects',
                            project_list=project_list)


@app.route('/art')
def art():
    return render_template('art.html', active_page='art')


@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Message sent successfully.\nName: {form.name.data}\nEmail: {form.email.data}\nMessage: \"{form.message.data}\"', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully made for {form.username.data}.', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', active_page='register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Login Successful. Welcome, {user.username}!', 'success')
            # checking for different redirect after user login
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('login'))
        else:
            flash(f'Account for email {form.email.data} does not exist.', 'danger')
    return render_template('login.html', active_page='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html', active_page='secret')
