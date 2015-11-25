from flask import Flask, render_template
import sys, requests, ast
app = Flask(__name__, template_folder="templates")

@app.route('/')
def car2go():
    r = requests.get("https://www.car2go.com/api/v2.0/vehicles?loc=austin&format=json")
    cars = []
    lats = []
    longs = []
    add_fuel = []
    for car in r.json()['placemarks']:
        if int(car['fuel']) <= 25:
            cars.append(car)
    for car in cars:
        car['coordinates'] = ast.literal_eval(car['coordinates'])
        lats.append(car['coordinates'][0])
        longs.append(car['coordinates'][1])
        add_fuel.append(car['address'] + ", fuel: " + car['fuel'])
    print(cars[0])
    print(lats[0])
    print(longs[0])
    print(add_fuel[0])
    return render_template("index.html", lats=lats, longs=longs, add_fuel=add_fuel)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)