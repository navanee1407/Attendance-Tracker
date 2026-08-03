import mysql.connector
import datetime
from datetime import date


mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='school')
mycursor=mydb.cursor()

today=datetime.datetime.now().strftime('%d/%m/%Y-%H:%M')
today_table_name = datetime.date.today().strftime('%d/%m/%Y')

create_today_table_query = f""" 
create table if not exists `{today_table_name}`(
    rollnumber int(5),
    studentName varchar(50),
    time varchar(10),
    Status varchar(10)
)
"""
mycursor.execute(create_today_table_query)

rollNumber=input('Scan the barcode:')

select_query='select * from student_details'
mycursor.execute(select_query)
data=mycursor.fetchall()
for i in data:
    print(i)


