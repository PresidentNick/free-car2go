from flask import Flask, render_template
import sys
app = Flask(__name__, template_folder="templates")

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))