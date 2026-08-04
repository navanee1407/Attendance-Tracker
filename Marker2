import mysql.connector
import datetime
from datetime import date


mydb=mysql.connector.connect(host='localhost',user='root',password='admin',database='school')
mycursor=mydb.cursor()

today=datetime.datetime.now().strftime('%d/%m/%Y-%H:%M')
today_table_name = datetime.date.today().strftime('%d_%m_%Y')


def create_today_table():
    create_today_table_query = f""" 
    create table if not exists `{today_table_name}`(
        rollnumber int(5) primary key,
        studentName varchar(50),
        Attendance_time varchar(20),
        Status varchar(10)
    )
    """
    mycursor.execute(create_today_table_query)

def mark_present():
    select_studentDetails_query='select * from student_details'
    mycursor.execute(select_studentDetails_query)
    data=mycursor.fetchall()

    rollNumber=int(input('Scan the barcode:'))
    
    select_present_data_query=f'select * from {today_table_name} where rollnumber=%s'
    mycursor.execute(select_present_data_query,(rollNumber,))
    present_data=mycursor.fetchone()

    if present_data is None :
        for i in data:
            if i[0] == rollNumber:
                studentName=i[1]
                Status = 'Present'
                

        insert_query = f'insert ignore into `{today_table_name}` values (%s,%s,%s,%s)'
        insert_values = (rollNumber,studentName,today,Status)

        mycursor.execute(insert_query,insert_values)
        mydb.commit()

        print(f'Attendance marked for {studentName}')

    elif present_data[3]=='Absent':
        change=input('Student marked Absent does changes required?(y/n)')
        if change.lower()=='y':
            update_query=f"update {today_table_name} set status='Present',Attendance_time=%s where rollnumber=%s"
            mycursor.execute(update_query,(today,rollNumber))
            mydb.commit()
            print('Changes made successfully')
        else:
            pass
def mark_absent():
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
    
    

create_today_table()

print("'1' for Mark Attendance")
print("'2' for Close Attendance")
cont='y'
while (cont.lower()=='y'):
    
    opt=int(input('Choose your option:'))
    if opt==1:
        mark_present()
    elif opt==2:
        mark_absent()
    cont=input('Do you want to continue(y/n:)')