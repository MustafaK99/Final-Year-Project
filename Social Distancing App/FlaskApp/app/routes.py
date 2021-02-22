from flask import render_template, url_for, flash, redirect
from app import app, dataScraper
from app.forms import RegistrationForm, LoginForm
from app.models import User, Detections


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}', 'Success')
        return redirect(url_for('welcome'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'logged in', 'Success')
        return redirect(url_for('welcome'))
    return render_template('login.html', title='login', form=form)
