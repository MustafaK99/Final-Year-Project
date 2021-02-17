from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import dataScraper

app = Flask(__name__)

app.config['SECRET_KEY'] = '6e42af73537c607675cb4cc78e3959e8'


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


@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run()
