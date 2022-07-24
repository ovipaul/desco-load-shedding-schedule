from re import A
from aem import Query
import mysql.connector
import pandas as pd
import csv


mydb = mysql.connector.connect(host="localhost", password="paul", user="root", database="load_shedding")

# load_shedding_schedule data insertion

with open('data-analyst-task/load_shedding_schedule.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_value=[]
    for row in csvfile:
        value = (row[0], row[1])
        all_value.append(value)
        
del all_value[0]

query = "Insert INTO load_shedding_schedule(area_id, time) VALUES (%s, %s)"

mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()

print('load_shedding_schedule table data inserted successfully')




# users data insertion #
with open('data-analyst-task/users.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_value=[]
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4])
        all_value.append(value)
        
del all_value[0]
query = "Insert INTO users(ID,name,email,location,created_at) VALUES (%s, %s, %s, ST_GeomFromText(%s), STR_TO_DATE(%s, '%m/%d/%Y'))"

mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()

print('users table data inserted successfully')


# area_map data insertion #
with open('data-analyst-task/area_map.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_value=[]
    for row in csvfile:
        value = (row[0], row[1], row[2])
        all_value.append(value)
        
del all_value[0]
query = "Insert INTO area_map(ID,area_name,polygon) VALUES (%s, %s, ST_PolyFromText(%s,0))"

mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()

print('area_map table data inserted successfully')