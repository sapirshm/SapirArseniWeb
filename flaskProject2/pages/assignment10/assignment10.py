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


alert_change = ""

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/', template_folder='templates')

@app.route("/assignment10", methods=['GET', 'POST'])
def assignment10_page():
    global  alert_change
    alert_change = ""
    return render_template('assignment10.html')


app.register_blueprint(assignment10)

# insert
@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    global  alert_change
    alert_change = "The user "+name+" is inserted"
    return redirect('/user_list')

# update
@app.route('/update_user', methods=['POST'])
def update_user_func():
    name = request.form['name']
    new_email = request.form['new_email']
    query = "update users set email = '%s' where name = '%s'" % (new_email, name)
    interact_db(query=query, query_type='commit')
    global alert_change
    alert_change = "The email of the user "+name+" is updated"
    return redirect('/user_list')

# delete
@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s'" % name
    interact_db(query, query_type='commit')
    global  alert_change
    alert_change = "The user "+name+" was deleted"
    return redirect('/user_list')

# display
@app.route('/user_list')
def user_list_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', user_list=query_result,  alert_change= alert_change)
if __name__ == '__main__':
    app.run(debug=True)