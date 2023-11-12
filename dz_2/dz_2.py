import secrets

from flask import Flask, redirect, render_template, request,  make_response, url_for

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    return render_template('base.html')


@app.get('/login/')
def login_get():
    cookie_name = request.cookies.get('username')
    if cookie_name:
        return redirect(url_for('greeting', name=cookie_name), 302)
    else:
        return render_template('login.html')


@app.post('/login/')
def login_post():
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        response = make_response(redirect(url_for('greeting', name=name), 302))
        response.headers['new_head'] = 'new_value'
        response.set_cookie('username', name)
        return response
    else:
        return render_template('login.html')


@app.route('/greeting/<name>/')
def greeting(name):
    cookie_name = request.cookies.get('username')
    if cookie_name == name:
        return render_template('greeting.html', name=name)
    else:
        return render_template('login.html')


@app.route('/logout/')
def logout():
    response = make_response(render_template('base.html'))
    response.set_cookie('username', 'None', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
