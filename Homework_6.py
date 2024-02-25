########## Task 1 ############
### Question 1 ###
import psycopg2
import pandas as pd
import xlrd
import os
from sqlalchemy import create_engine

os.getcwd()
os.chdir(r'C:\Users\dudul\OneDrive\Documents\Dudu\Programming\Py4Econ\Introduction_Python\6_Data_sql\data')
df = pd.read_excel("data.xlsx")
data = [tuple(row) for row in df.values]

connection = psycopg2.connect(
        user = "postgres",
        password = "Iveel724",
        host = "localhost", # 198.16.16.01, 127.0.0.1, www.prod.xxxcompany.com/serverdb
        port = "5432",
        database = "week6"
    )

cursor = connection.cursor()
#cursor.execute("SELECT * from datacsv;")
#record = cursor.fetchall()

cursor.execute("""CREATE TABLE data
(
    id integer NOT NULL PRIMARY KEY,
    firstName text NOT NULL,
    lastName text,
    citizenId text,
    age integer
);""")
connection.commit()

cursor.executemany("""INSERT INTO data
(id,firstname,lastname,citizenid,age)
VALUES (%s,%s,%s,%s,%s)""", data)
connection.commit()


### Question 2 ###

cursor.execute("""SELECT firstname, lastname
FROM data
LIMIT 3;""")
connection.commit()

record = cursor.fetchall()
for row in record:
    print(row)

### Question 3 ###
cursor.execute("""SELECT firstname, age
FROM data
ORDER BY id DESC
LIMIT 3;""")
connection.commit()

record = cursor.fetchall()
for row in record:
    print(row)


cursor.close()
connection.close()
