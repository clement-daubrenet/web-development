from flask import Flask, render_template


weather = Flask(__name__)


@weather.route('/')
def main_page():
    return render_template("main.html", name="moi")


@weather.route('/temperature')
def temperatures():
    pass


@weather.route('/forecast')
def forecast():
    pass
