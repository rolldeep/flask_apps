
from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def main():
    list_tours = [tour for tour in data.tours.values()]
    return render_template('index.html',
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           departures=data.departures,
                           tours_list=list_tours[:6])


@app.route('/departures/<departure>')
def show_departure(departure):
    tours_list = [tour for i, tour in data.tours.items() if tour['departure'] == departure]
    vals = [tour['price'] for tour in tours_list]
    nights = [tour['nights'] for tour in tours_list]
    cnt = len(tours_list)
    return render_template('departure.html',
                           departures=data.departures,
                           departure=data.departures[departure],
                           tours_list=tours_list,
                           cnt=cnt,
                           min_val=min(vals),
                           max_val=max(vals),
                           min_nights=min(nights),
                           max_nights=max(nights))


@app.route('/tours/<tour_id>')
def show_tour(tour_id):
    stars_string = "*" * int(data.tours[int(tour_id)]['stars'])
    return render_template('tour.html', tour_id=tour_id, tours=data.tours, departures=data.departures, stars=stars_string)


if __name__ == "__main__":
    app.run()
