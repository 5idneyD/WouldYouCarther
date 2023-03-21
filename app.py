from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__, static_folder="dist")
CORS(app)


@app.route('/')
def index():
    a = 7
    return render_template('index.html', a=a)

if __name__=="__main__":
    app.run(debug=True)