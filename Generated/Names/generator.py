import sqlite3 as sql
from random import randrange

with sql.connect("names.db") as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS people(
id integer PRIMARY KEY,
name text,
sex text,
age integer,
bday integer,
job text,
street text,
country text,
company text);''')

files = [
    "country",
    "fname",
    "gender",
    "jobs",
    "bday",
    "sname",
    "street",
    "workplace"
]
raw = {}
for filename in files:
    with open(f"Generated/Names/Text/{filename}.txt") as file:
        raw[filename] = file.read().splitlines()

for i in range(len(raw["jobs"])):
    cursor.execute(f'''INSERT INTO people(id,name,sex,age,bday,job,street,country,company)
VALUES("{i + 1}", "{raw["fname"][i]} {raw["sname"][i]}", "{"male" if raw["gender"][i].capitalize().strip() == "True" else "female"}", "{randrange(18, 65)}", "{raw["bday"][i][:11].strip()}", "{raw["jobs"][i]}", "{raw["street"][i]}", "{raw["country"][i]}", "{raw["workplace"][i]}")''')
db.commit()

db.close()