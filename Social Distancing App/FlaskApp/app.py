from flask import Flask, render_template
import dataScraper

app = Flask(__name__)


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
    return 'Covid 19 data by region/county'


if __name__ == '__main__':
    app.run()
