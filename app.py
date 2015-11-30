from flask import Flask, render_template
import sys, requests, ast
app = Flask(__name__, template_folder="templates")

@app.route('/')
def car2go():
    r = requests.get("https://www.car2go.com/api/v2.0/vehicles?loc=austin&format=json")
    cars = []
    coords = []
    add_fuel = []
    for car in r.json()['placemarks']:
        if int(car['fuel']) <= 25:
            cars.append(car)
    for car in cars:
        car['coordinates'] = ast.literal_eval(car['coordinates'])
        latlon = [car['coordinates'][0], car['coordinates'][1]]
        coords.append(latlon)
        add_fuel.append(car['address'] + ", fuel: " + car['fuel'])
    return render_template("index.html", coords=coords, add_fuel=add_fuel)

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port, debug=True)