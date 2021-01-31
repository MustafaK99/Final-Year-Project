from flask import Flask

app = Flask(__name__)


@app.route('/home')
@app.route('/index')
@app.route('/')
def welcome():
    return 'welcome'


@app.route('/about')
def about():
    return 'About the Covid-19 analysis platform'


@app.route('/country')
@app.route('/nation')
def nation():
    return 'Covid-19 data by nation'


@app.route('/county')
@app.route('/region')
def region():
    return 'Covid 19 data by region/county'


if __name__ == '__main__':

    app.run()
