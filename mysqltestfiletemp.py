from tkinter import *
import mysql.connector
import sys 

print(sys.executable)
root=Tk()
root.title("mysql_gui")
root.geometry("300x250")

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmay",
    database="test"
)

c=db.cursor()

#c.execute("CREATE DATABASE TEST")
#creating table
'''
c.execute("""CREATE TABLE employee(
          emp_id INT,
          first_name text,
          last_name text,
          salary INT)
          """)
'''
def submit():
    #connecting to a database
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmay",
    database="test"
     )
    c=db.cursor()

     #inserting values
    c.execute("INSERT INTO employee VALUES(:emp_id, :first_name, :last_name, :salary)",
            {
        'emp_id': emp_id.get(),
        'first_name': first_name.get(),
        'last_name': last_name.get(),
        'salary': salary.get()
           })
    #clearing text boxes
    emp_id.delete(0,END)
    first_name.delete(0,END)
    last_name.delete(0,END)
    salary.delete(0,END)

'''def query():
    #creating connection again
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmay",
    database="test"
     )
    c=db.cursor()
    #fetching data
    c.execute("SELECT *,oid FROM employee")
    records=c.fetchall()
    print(records)
'''


   
#labels
emp_id=Label(root, text="user id")
emp_id.grid(row=0,column=0,padx=20)
first_name=Label(root, text="first name")
first_name.grid(row=1,column=0)
last_name=Label(root, text="last name")
last_name.grid(row=2,column=0)
salary=Label(root, text="salary")
salary.grid(row=3,column=0)

#entry widgets
emp_id=Entry(root,width="30")
emp_id.grid(row=0,column=1)
first_name=Entry(root,width="30")
first_name.grid(row=1,column=1)
last_name=Entry(root,width="30")
last_name.grid(row=2,column=1)
salary=Entry(root,width="30")
salary.grid(row=3,column=1)

#submit button
submit_btn=Button(root,text="submit",command=submit)
submit_btn.grid(row=4,column=0,columnspan=2,padx=10,pady=10,ipadx=100,ipady=12)

#creating query button to show records
'''query_btn=Button(root,text="show records")
query_btn.grid(row=5,column=0,columnspan=2,padx=10,pady=10,ipadx=100,ipady=12)
'''
root.mainloop()
