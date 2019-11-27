from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')


@app.route('/art')
def art():
    return render_template('art.html', active_page='art')


@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')


if __name__ == '__main__':
    app.run(debug=True)
