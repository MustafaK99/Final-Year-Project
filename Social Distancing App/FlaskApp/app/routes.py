from flask import render_template, url_for, flash, redirect, request, Response
from app.social_distance_advanced import Detection
from app import app, dataScraper, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdatedAccountInfoForm
from app.models import User, Detections
from flask_login import login_user, current_user, logout_user, login_required


detector = Detection()


@app.route('/home')
@app.route('/index')
@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/country')
@app.route('/nation')
def nation():
    area_name, new_cases, new_deaths = dataScraper.latestGraphByNation()
    return render_template('nation.html', area_name=area_name, new_cases=new_cases, new_deaths=new_deaths)


@app.route('/county')
@app.route('/region')
def region():
    return render_template('region.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created! please log in', 'Success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('welcome'))
        else:
            flash('Login Unsuccessful, email and/or password are incorrect please try again', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('welcome'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdatedAccountInfoForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account info has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route("/detection")
@login_required
def new_detection():
    return render_template('detection.html', title='New detection')


def gen(social_distance_advanced):
    while True:
        frame = social_distance_advanced.startProcess()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route("/video_feed")
@login_required
def video_feed():
    return Response(gen(detector),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
