from flask import render_template, url_for, flash, redirect
from flaskapp.models import User
from flaskapp.forms import Register
from flaskapp import app, db, cot
from datetime import datetime


@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, email=form.email.data, city=form.city.data)
        db.session.add(new_user)
        db.session.commit()
        app.logger.info(
            f'User with name {new_user.name} and email {new_user.email} created at {datetime.now(cot)}')
        flash(message='User created!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
