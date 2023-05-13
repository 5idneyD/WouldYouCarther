import json
import sqlite3

conn = sqlite3.Connection("./database/databse.db")
c = conn.cursor()

c.execute("DROP TABLE Cars;")
c.execute("CREATE TABLE Cars (row, make, model);")
c.execute("CREATE TABLE Records (row, winner, loser);")

with open("./data.json", "r") as f:
    data = json.load(f)

cars = 0
for make, models in data.items():
    for model in models:
        print(f"{make}: {model}")
        model = model.replace("'", "?")
        cars += 1
        c.execute(f"INSERT INTO Cars VALUES ('{cars}', '{make}', '{model}');")

for i in c.execute("SELECT row FROM Cars;"):
    print(i)
conn.commit()
conn.close()