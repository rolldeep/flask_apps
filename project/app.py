
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def show_departure():
    return render_template('tour.html')


@app.route('/tours/<id>/')
def show_tour():
    return render_template('tour.html')


if __name__ == "__main__":
    app.run()
