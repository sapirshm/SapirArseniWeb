from flask import Flask, redirect, url_for
app = Flask (__name__)


@app.route('/')
def mainpage_func():
    return 'Welcome To Homepage'


@app.route('/home')     #using redirect function
def home_func():
    return redirect('/')


@app.route('/catalog')
def catalog_func():
    return 'This Is The Catalog Page'


@app.route('/productcatalog')      #using redirect + url function
def catatlog2_func():
    return redirect(url_for('catalog_func'))


if __name__ == '_main_':
    app.run(debug=True)