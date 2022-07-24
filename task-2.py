import mysql.connector
import pandas as pd
import csv


mydb = mysql.connector.connect(host="localhost", password="paul", user="root", database="load_shedding")

mycursor = mydb.cursor()
mycursor.execute("select * from users order by created_at desc")
user_data = mycursor.fetchall()

df = pd.DataFrame (user_data, columns = ['ID','name','email','location','created_at'])
df = df.drop_duplicates(subset=['email'], keep='first')
df.to_csv('unique_user_data.csv', sep=',', header=True, index=False)