from flask import Flask, redirect, url_for, render_template, request,session,Blueprint
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'

users = {'user1': {'name': 'Yossi', 'email': 'yo@gmail.com'},
         'user2': {'name': 'Sapir', 'email': 'sapir@gmail.com'},
         'user3': {'name': 'Mika', 'email': 'mika@gmail.com'},
         'user4': {'name': 'Inbar', 'email': 'inbar@gmail.com'},
         'user5': {'name': 'Aviv', 'email': 'aviv@gmail.com'},
         }

@app.route("/")
@app.route("/CV")
def cv_page():
    return render_template('CV.html')


@app.route("/assignment8")
def assignment8_page():
    name = ''
    last_name = ''
    return render_template('Assignment8.html',
                           name=name,
                           last_name=last_name,
                           profile={'Hobbie1': 'Dance',
                                   'Hobbie2': 'Hockey'})



@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9_page():
    # search form
    if 'email' in request.args:
        email = request.args['email']
        if email == '':
            return render_template('assignment9.html', user_list=users)
        # search it in users dict
        for key, value in users.items():
            if value.get('email') == email:
                return render_template('assignment9.html', u_name=value.get('name'), u_email=value.get('email'))
    # registration form
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
    return render_template('assignment9.html')

@app.route("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run(debug=True)