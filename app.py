from flask import Flask, render_template
from flask_cors import CORS
import json
from flask_sqlalchemy import SQLAlchemy
import os
import random

app = Flask(__name__, template_folder="src/templates", static_folder="dist")
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\Dev\WebDev\catch\database\database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SESSION_PERMANENT"] = False
app.config["SECRET_KEY"] = os.urandom(12).hex()
app.secret_key = os.urandom(12).hex()

db = SQLAlchemy(app)

class Cars(db.Model):
    __tablename__ = "Cars"
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(16), nullable=False)
    model = db.Column(db.String(32), nullable=False)
    img = db.Column(db.String)

class Records(db.Model):
    __tablename__ = "Records"
    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.String, db.ForeignKey("Cars.id"))
    loser = db.Column(db.String, db.ForeignKey("Cars.id"))


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    
    
    # with open("./database/data.json", "r") as q:
    #     data = json.loads(q.read())
    
    # for info, href in data.items():
    #     br = info.index("?")
    #     make = info[:br]
    #     model = info[br+1:]
    #     img_link = href
    #     car = Cars(make=make, model=model, img=img_link)
    #     db.session.add(car)
    # db.session.commit()
    
    
    number_of_cars = len(Cars.query.all())

    first_car = Cars.query.filter(Cars.id==str(random.randint(1, number_of_cars))).first()
    second_car = Cars.query.filter(Cars.id==str(random.randint(1, number_of_cars))).first()
    
    return render_template('index.html', first_car=first_car, second_car=second_car)

if __name__=="__main__":
    app.run(debug=True)