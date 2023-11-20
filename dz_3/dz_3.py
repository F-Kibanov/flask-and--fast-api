import secrets

from flask import Flask, render_template, request, make_response
from flask_wtf.csrf import CSRFProtect

from forms import RegistrationForm
from model import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
@app.route('/main/')
def main():
    return render_template('base.html')


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('Database Users created!')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.user_name.data
        surname = form.user_surname.data
        email = form.email.data
        hashed_password = hash(form.password.data)
        user = (name, surname, email, hashed_password)
        user = User(name=name, surname=surname, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return render_template('registered.html')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
