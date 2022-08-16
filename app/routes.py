from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user,login_required,logout_user



@app.route('/home')
@app.route('/')
def home():
    
    return 'Hello World!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':


        user=User(username=request.form['username'],email=request.form['email'],
            password_hash=generate_password_hash(request.form['password']))
        db.session.add(user)
        db.session.commit()
        return render_template('login.html')
    flash('Your account has been created!', 'success')
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            if check_password_hash(user.password_hash, request.form['password']):
                login_user(user, remember=True)
            return redirect(url_for('home'))
        flash('invalid Username or Password')
        return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))