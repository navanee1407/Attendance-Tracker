import mysql.connector
import datetime
from datetime import date


mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='school')
mycursor=mydb.cursor()

today=datetime.datetime.now().strftime('%d/%m/%Y-%H:%M')
today_table_name = datetime.date.today().strftime('%d_%m_%Y')

create_today_table_query = f""" 
create table if not exists `{today_table_name}`(
    rollnumber int(5) primary key,
    studentName varchar(50),
    Attendance_time varchar(20),
    Status varchar(10)
)
"""
mycursor.execute(create_today_table_query)

select_studentDetails_query='select * from student_details'
mycursor.execute(select_studentDetails_query)
data=mycursor.fetchall()
list_records=[]

for i in data:
    list_data=[i[0],i[1]]
    list_records.append(list_data)

print("'1' for Mark Attendance")
print("'2' for Close Attendance")
cont='y'

while cont.lower()=='y':

    opt=int(input('Choose your option:'))

    if opt==1:

        rollNumber=int(input('Scan the barcode:'))

        select_present_query = f'select * from {today_table_name}'
        mycursor.execute(select_present_query)
        present_data= mycursor.fetchall()

        for i in present_data:
            if i[0]==rollNumber:
                print(f'Attendance already marked for {i[1]}')
                cont=input('Do you want to continue(y/n:)')

            elif i[3] == 'Absent':
                change=input('Student marked absent, do you need to change it(y/n):')
                if change.lower()=='y':
                    update_query=f"update {today_table_name} set Attendance_time={today},Status='Present' where rollnumber={rollNumber}"
                    
            else:

                for j in list_records:
                    if j[0] == rollNumber:
                        studentName=j[1]
                        Status = 'Present'

                insert_query = f'insert into `{today_table_name}` values (%s,%s,%s,%s)'
                insert_values = (rollNumber,studentName,today,Status)

                mycursor.execute(insert_query,insert_values)
                mydb.commit()

                print(f'Attendance marked for {studentName}')
                cont=input('Do you want to continue(y/n:)')

    if opt==2:

        select_absent_query = f'select A.rollNumber,A.studentName,B.Attendance_time,B.Status from student_details A left join {today_table_name} B on A.rollNumber=B.rollNumber'
        mycursor.execute(select_absent_query)
        absent_data=mycursor.fetchall()

        for i in absent_data:
            if i[3] == None:
                Status = 'Absent'
                rollNumber=i[0]
                studentName=i[1]

        insert_absent_query = f'insert into {today_table_name} (rollNumber,studentName,Status) values (%s,%s,%s)'
        insert_absent_values = (rollNumber,studentName,Status)

        mycursor.execute(insert_absent_query,insert_absent_values)
        mydb.commit()
        print('Attendance closed successfully')
        cont=input('Do you want to continue(y/n:)')