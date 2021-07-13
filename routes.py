from app import app, db, login
from flask import request, render_template, flash, redirect,url_for
from models import User, Post, Like
from forms import RegistrationForm, LoginForm, DestinationForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('plans'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("user", username=current_user.username)
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('plans')) 
    form = RegistrationForm()
    if form.validate_on_submit():
        user1 = User.query.filter_by(username=form.username.data).first()
        if user1 is not None:
            flash('Please use a different username')
            return redirect(url_for('register'))

        user2 = User.query.filter_by(email=form.email.data).first()
        if user2 is not None:
            flash('Please use a different email address')
            return redirect(url_for('register'))
        
        if '@' not in form.email.data:
            flash('Please enter a valid email address')
            return redirect(url_for('register'))

        if form.password.data != form.password2.data:
            flash('Please make sure passwords match')
            return redirect(url_for('register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("login")
        return redirect(next_page)
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>',methods=['GET', 'POST'])
@login_required
def user(username):
    user = current_user
    user = User.query.filter_by(username=user.username).first()
    posts = Post.query.filter_by(user_id=user.id)
    length = Post.query.filter_by(user_id=user.id).count()
    if posts is None:
        posts = []
    form = DestinationForm()
    if request.method == 'POST' and form.validate():
        new_destination = Post(city = form.city.data,country=form.country.data,description=form.description.data, user_id=current_user.id)
        db.session.add(new_destination)
        db.session.commit()
        return redirect (url_for("authplans", username=user.username))
    return render_template('user.html', user=user, posts=posts, form=form, length=length)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/plans')
def plans():
    posts = Post.query.all()
    if not posts:
        posts=[]
    return render_template('plans.html', posts=posts)

@app.route('/<username>/plans')
@login_required
def authplans(username):
    posts = Post.query.all()
    if not posts:
        posts=[]
    return render_template('authplans.html', posts=posts)

@app.route('/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(url_for("authplans", username=current_user.username))

@app.route('/<int:post_id>/')
@login_required
def delete(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    current_user.delete_post(post)
    db.session.commit()
    return redirect(url_for("user", username=current_user.username))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


