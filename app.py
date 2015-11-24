from flask import Flask, render_template
import sys, requests, ast
app = Flask(__name__, template_folder="templates")

@app.route('/')
def car2go():
    r = requests.get("https://www.car2go.com/api/v2.0/vehicles?loc=austin&format=json")
    cars = []
    for car in r.json()['placemarks']:
        if int(car['fuel']) <= 25:
            cars.append(car)
    for car in cars:
        car['coordinates'] = ast.literal_eval(car['coordinates'])
    print(type(cars[0]['coordinates']))
    print(cars[0]['coordinates'])
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)