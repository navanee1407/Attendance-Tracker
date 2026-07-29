import os
import barcode
from barcode.writer import ImageWriter
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='admin')
mycursor = mydb.cursor()

mycursor.execute('Create database School')
mycursor.execute('Create table Student_details(
rollNumber int
studentName varchar)')

rollNumber = input("Enter the student roll number: ")
studentName = input('Enter the student name:')

# Get the folder where this script is located
script_folder = os.path.dirname(os.path.abspath(__file__))

barcode_class = barcode.get_barcode_class('code128')
my_barcode = barcode_class(rollNumber, writer=ImageWriter())

filename = os.path.join(script_folder, f"student_{rollNumber}")
saved_path = my_barcode.save(filename)

print(f"Barcode successfully saved as: {saved_path}")