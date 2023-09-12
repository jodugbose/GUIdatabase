import pyodbc

def insert():
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-211201-256\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    Name = E1.get()
    Course_Code = "GEG 101"
    Mark = int(E2.get())

    Grade = "F"
    
    if Mark >= 55:
        Grade = "C"
    
    if Mark >= 65:
        Grade = "B"
    
    if Mark >= 75:
        Grade = "A"
  
    cur.execute("insert into Training.dbo.Students(name,course_code,mark,grade) values (?,?,?,?)", (Name,Course_Code,Mark,Grade))
    cur.commit()
    print('baddo')



def update():
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-211201-256\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    name = E1.get()
    mark = E2.get()
    cur.execute("update Training.dbo.Students set mark = ? where name = ? ",(mark,name))
    cur.commit()
    print("successful")

def delete():
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-211201-256\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    name = E1.get()
    cur.execute("delete from Training.dbo.Students where name = ?",(name))
    cur.commit()
    print("successful")

def list():
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-211201-256\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cur = conn.cursor()
    lb1.delete(0,END)   
    cur.execute("select * from Training.dbo.Students")
    for row in cur:
        lb1.insert(0,f"{row}\n")
    cur.commit()
    print("successful")

def save():
    conn =  pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-211201-256\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')
    cursor = conn.cursor()
    status_dict = {"A": 'automatic employment', "B": 'open to work', "C" : 'open to work', "F": 'probation'}
    fetch_query = "SELECT * FROM Training.dbo.Students WHERE employment_status is NULL"
    rows = cursor.execute(fetch_query)
        # print(rows)
    for row in rows:
        update_query = "UPDATE Students SET employment_status=? WHERE grade = ?"
        grade = row[4].strip()
        cursor.execute(update_query, (status_dict[grade], grade))
        cursor.commit()
        conn.close()
            
    print("Employment Status set successfully")

from tkinter import *

root = Tk()
root.title("Fill in Students Record")
root.geometry("200x200")

L1 = Label(root,text="Name:",fg="Black",font=("Arial",14))
L2 = Label(root,text="Mark:",fg="Black",font=("Arial",14))
B1 = Button(root,text="Insert",bg="White",fg="Black",width=10,command=insert)
B2 = Button(root,text="Update",bg="White",fg="Black",width=10,command=update)
B3 = Button(root,text="Delete",bg="White",fg="Black",width=10,command=delete)
B4 = Button(root,text="List",bg="White",fg="Black",width=10,command=list)
B5 = Button(root,text="Save",bg="White",fg="Black",width=10,command=save)
E1 = Entry(root,show=None,width=80,bd=3)
E2 = Entry(root,show=None,width=80,bd=3)
lb1 = Listbox(root,highlightbackground="Green",height=30,width=100,bd=3)


L1.place(x=5,y=10)
L2.place(x=5,y=50)
E1.place(x=70,y=15)
E2.place(x=70,y=55)
lb1.place(x=5,y=130)
B1.place(x=5,y=620)
B2.place(x=100,y=620)
B3.place(x=200,y=620)
B4.place(x=300,y=620)
B5.pack(anchor=S)
root.mainloop()




        



