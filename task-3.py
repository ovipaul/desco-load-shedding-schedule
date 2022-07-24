import email
from re import A
from aem import Query
import mysql.connector
import pandas as pd
import csv
from shapely.geometry import Point, Polygon
mydb = mysql.connector.connect(host="localhost", password="paul", user="root", database="load_shedding")

mycursor = mydb.cursor()
mycursor.execute("select * from area_map")
area_map = mycursor.fetchall()
area_map = pd.DataFrame(area_map, columns = ['ID','area_name','polygon'])

mycursor = mydb.cursor()
mycursor.execute("select * from load_shedding_schedule")
load_shedding_schedule = mycursor.fetchall()
load_shedding_schedule = pd.DataFrame(load_shedding_schedule, columns = ['area_id','time'])

mycursor = mydb.cursor()
mycursor.execute("select * from users")
users = mycursor.fetchall()
users = pd.DataFrame(users, index=None, columns = ['ID','name','email','location','created_at'])

name = 'Davis'
email = 'davis@gmail.com'

usr_data = users.loc[users['name'] == name]
e_check=usr_data.loc[:,"email"].values[0]


if email == e_check:
    usr_location=usr_data.loc[:,"location"].values[0]
    
    for index, row in area_map.iterrows():
        coords= row[2]
        poly = Polygon(coords)
        if(usr_location.within(poly)):
            print("Found Location")
            area_id=row[0]

usr_data = load_shedding_schedule.loc[load_shedding_schedule['area'] == area_id]
load_shedding_time=load_shedding_schedule.loc[:,"time"].values[0]

print("Load Shedding Time:")
print(load_shedding_time)