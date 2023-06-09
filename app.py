from flask import Flask, render_template, request
from flask_cors import CORS
import json
from flask_sqlalchemy import SQLAlchemy
import os
import random
import numpy as np
import time

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

@app.route('/', methods=["POST", "GET"])
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
    
    

    
    if request.method == "POST":
        time.sleep(3)
        try:
            winner = request.form["car1"]
            loser = request.form["car1loser"]
        except:
            winner = request.form["car2"]
            loser = request.form["car2loser"]
            
            
        winner_make = winner[:winner.index(",")]
        winner_model = winner[winner.index(",")+2:]
        winner_id = Cars.query.filter(Cars.make==winner_make, Cars.model==winner_model).first().id
        loser_make = loser[:loser.index(",")]
        loser_model = loser[loser.index(",")+2:]
        loser_id = Cars.query.filter(Cars.make==loser_make, Cars.model==loser_model).first().id
        
        print("Winner: ", winner_make)
        print("Loser: ", loser_make)
        
        record = Records(winner=winner_id, loser=loser_id)
        db.session.add(record)
        db.session.commit()
    
    number_of_cars = len(Cars.query.all())

    first_car = Cars.query.filter(Cars.id==str(random.randint(5,10))).first()
    second_car = Cars.query.filter(Cars.id==str(random.randint(11,25))).first()
    
    records = Records.query.filter(((Records.winner==first_car.id) & (Records.loser==second_car.id)) | ((Records.winner==second_car.id) & (Records.loser==first_car.id))).all()
    
    first_car_wins = 0
    second_car_wins = 0
    total_records = 0
    for record in records:
        if int(record.winner) == int(first_car.id):
            first_car_wins += 1
        else:
            second_car_wins += 1
        total_records += 1

    try:
        first_car_wins = np.round(first_car_wins / total_records * 100, 2)
    except:
        first_car_wins = 50
    try:
        second_car_wins = np.round(second_car_wins / total_records * 100, 2)
    except:
        second_car_wins = 50
        
    return render_template('index.html', first_car=first_car, second_car=second_car, first_car_wins=first_car_wins, second_car_wins=second_car_wins, total_records=total_records)

if __name__=="__main__":
    app.run(debug=True)