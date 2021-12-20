from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route("/")
@app.route("/CV")
def cv_page():
    return render_template('CV.html')


@app.route("/assignment8")
def assignment8_page():
    name = 'Sapir'
    last_name = 'Shmuelevitz'
    return render_template('Assignment8.html',
                           name=name,
                           last_name=last_name,
                           profile={'Hobbie1': 'Dance',
                                   'Hobbie2': 'Hockey'})