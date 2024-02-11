import sqlite3

#connect to sqlite
connection = sqlite3.connect("student.db")

#create a cursor to retrieve records, insert records, create tables
cursor = connection.cursor()

#create the table that
table_info = """
Create table student(Name VARCHAR(25),
Class Varchar(25),
Section Varchar(25),
Marks INT);
"""
cursor.execute(table_info)

#Insert records in the table
cursor.execute('''insert into student values('Asif Khan', 'Data Science', 'A', 98)''')
cursor.execute('''insert into student values('Abhishek Raik', 'Data Analytics', 'B', 90)''')
cursor.execute('''insert into student values('Nethon', 'Management', 'A', 96)''')
cursor.execute('''insert into student values('Jack Ma', 'Director', 'A', 99)''')
cursor.execute('''insert into student values('Jeff Moon', 'Recruitment', 'C', 92)''')

#Display all the records
data = cursor.execute('''Select * from student''')

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()
