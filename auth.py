from flask import Blueprint,render_template,redirect,url_for,request
from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from flask_login import login_user,logout_user,login_required

auth = Blueprint('auth',__name__)



@auth.route('/login',methods=['GET','POST'])
def login_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password,password):
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.profile'))
    return render_template('login.html')

@auth.route('/signup', methods=['GET','POST'])
def signup_post():
    if request.method =='POST': 
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('main.index'))
        new_user = User(email = email, password=generate_password_hash(password,method='sha256'))
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
