import tkinter as tk 
import mysql.connector  
from tkinter import * 
import PIL 
   
  
def submitact(): 
      
    user = Username.get() 
    passw = password.get() 
   
    print(f"The name entered by you is {user} {passw}") 
   
    logintodb(user, passw) 
   
   
def logintodb(user, passw): 
      
    # If paswword is enetered by the  
    # user 
    if passw: 
        db = mysql.connector.connect(host ="localhost", 
                                     user = user, 
                                     password = passw, 
                                     db ="company") 
        cursor = db.cursor() 
          
    # If no password is enetered by the 
    # user 
    else: 
        db = mysql.connector.connect(host ="localhost", 
                                     user = user, 
                                     db ="company") 
        cursor = db.cursor() 
          
    # A Table in the database 
    savequery = "select * from employee"
      
    try: 
        cursor.execute(savequery) 
        myresult = cursor.fetchall() 
          
        # Printing the result of the 
        # query 
        for x in myresult: 
            print(x) 
        print("Query Excecuted succesfully") 
          
    except: 
        db.rollback() 
        print("Error occured") 
   
   
root = tk.Tk() 
root.geometry("300x150") 
root.title("DBMS Login Page") 
   
C = Canvas(root, height = 250, width = 300) 
  
# Definging the first row 
lblfrstrow = tk.Label(root, text ="Username -", ) 
lblfrstrow.place(x = 50, y = 20) 
  
Username = tk.Entry(root, width = 35) 
Username.place(x = 150, y = 20, width = 100) 
   
lblsecrow = tk.Label(root, text ="Password -") 
lblsecrow.place(x = 50, y = 50) 
  
password = tk.Entry(root, width = 35) 
password.place(x = 150, y = 50, width = 100) 
  
submitbtn = tk.Button(root, text ="Login",  
                      command = submitact) 
submitbtn.place(x = 125, y = 100, width = 55) 
  
root.mainloop() 