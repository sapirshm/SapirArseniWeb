from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/try_request")
def try_request_func():
    return request.method


@app.route("/home_page")
@app.route("/home")
@app.route("/")
def home_func():
    # DB
    found = False
    if found:
        return render_template('index.html',
                               name='Sapir',
                               last_name='Shmuelevitz')
    else:
        return render_template('index.html')


@app.route("/about", methods=['GET'])
def about_func():
    return render_template('about.html',
                           uni='BGU',
                           profile={'name': 'Sapir',
                                    'last_name': 'Shmuelevitz'},
                           degrees=['BSc.', 'Msc.'],
                           hobbies=('art', 'programming', 'teaching')
                           )


@app.route("/catalog", methods=['GET'])
def catalog_func():
    if 'product_type' in request.args:
        product_type = request.args['product_type']
        size = request.args['size']
        return render_template('catalog.html',p_type=product_type,p_size=size)
        return render_template('catalog.html')

@app.route('/login')
def login_func():
        return 'login page'

@app.route("/catalog_2", methods=['GET'])
def catalog2_func():
    return render_template('catalog_2.html')


if __name__ == '__main__':
    app.run(debug=True)

