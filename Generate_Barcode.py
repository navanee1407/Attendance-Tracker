import os
import barcode
from barcode.writer import ImageWriter
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='admin',database='school')
mycursor = mydb.cursor()

create_table_query='create table if not exists Student_details(rollNumber int(5) primary key, studentName varchar(50))'
mycursor.execute(create_table_query)

rollNumber = input("Enter the student roll number: ")
studentName = input('Enter the student name:')

# Get the folder where this script is located
script_folder = os.path.dirname(os.path.abspath(__file__))

barcode_class = barcode.get_barcode_class('code128')
my_barcode = barcode_class(rollNumber, writer=ImageWriter())

filename = os.path.join(script_folder, f"student_{rollNumber}")
saved_path = my_barcode.save(filename)

print(f"Barcode successfully saved as: {saved_path}")

insert_query ='insert into Student_Details values (%s,%s)'
insert_values= (rollNumber,studentName)
mycursor.execute(insert_query,insert_values)
mydb.commit()