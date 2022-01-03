from flask import redirect, render_template, request, Blueprint
from flaskProject2.interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')

alert_change = ""

@assignment10.route("/assignment10", methods=['GET', 'POST'])
def assignment10_page():
    global alert_change
    alert_change = ""
    return render_template('assignment10.html')


# insert
@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    global  alert_change
    alert_change = "The user "+name+" is inserted"
    return redirect('/user_list')

# update
@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    name = request.form['name']
    new_email = request.form['new_email']
    query = "update users set email = '%s' where name = '%s'" % (new_email, name)
    interact_db(query=query, query_type='commit')
    global alert_change
    alert_change = "The email of the user "+name+" is updated"
    return redirect('/user_list')

# delete
@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s'" % name
    interact_db(query, query_type='commit')
    global  alert_change
    alert_change = "The user "+name+" was deleted"
    return redirect('/user_list')

# display
@assignment10.route('/user_list')
def user_list_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', user_list=query_result,  alert_change= alert_change)