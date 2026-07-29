import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='admin',database='school')
mycursor = mydb.cursor()

query='create table if not exists Student_details(rollNumber int(5), studentName varchar(50))'
mycursor.execute(query)