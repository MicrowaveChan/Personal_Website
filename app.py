import csv
from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, LoginForm, ContactForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = '4f3c2b1a6c977eef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data/app.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    # unique userID
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    # toString
    def __repr__(self):
        return f'User \'{self.username}\' Email \'{self.email}\''


@app.route('/')
@app.route('/home')
def home():
    with open('static/data/skills.csv') as f:
        skill_list = list(csv.reader(f))[1:]
    return render_template('home.html', skill_list=skill_list)


@app.route('/projects')
def projects():
    with open('static/data/projects.csv') as f:
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
        if form.email.data == 'admin@test.com' and form.password.data == 'testing':
            flash(f'Welcome, admin.', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'Account for email {form.email.data} does not exist.', 'danger')
    return render_template('login.html', active_page='login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
