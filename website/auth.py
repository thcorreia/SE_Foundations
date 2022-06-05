from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/home")
def home():
    return render_template('home.html')
  
@auth.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    data = request.form
    print(data)
    return render_template('sign_in.html')

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        userName = request.form.get('userName')
        password1 = request.form.get('password1') 

        if len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(userName) < 2:
            flash('User name should be greater than 4 characters', category='error')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters', category='error')
        
        else:
            #new_user = User( email = email, userName = userName, password1=generate_password_hash(
             #   password1, method='sha256')) 
            #db.session.add(new_user)
           # db.session.commit()   
            flash('Account created!', category='success') 
            return redirect(url_for('views.home')) 

    return render_template('sign_up.html')

 


