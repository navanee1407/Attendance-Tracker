import mysql.connector
import datetime

mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='student_details')
mycursor=mydb.cursor()

today=datetime.datetime.now()

rollNumber=input('Scan the barcode:')

