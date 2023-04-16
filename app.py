from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__, template_folder="src/templates", static_folder="dist")
CORS(app)


@app.route('/')
def index():
    msg = "hello ReactPy"
    return render_template('index.html')

if __name__=="__main__":
    app.run()