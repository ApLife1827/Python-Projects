




from tkinter import *
import tkinter.font
import sqlite3

conn = sqlite3.connect("MyDB.db") #Connect to the DB

## ID          = TRACKING ID
## NAME        = NAME OF THE PERSON
## DEPARTURE   = STARTING ADDRESS OF PACKAGE
## DESTINATION = DELIVERY ADDRESS OF PACKAGE
## TYPE        = FAST DELIVERY OR NORMAL DELIVERY

##conn.execute("INSERT INTO DETAILS(ID,NAME,DEPARTURE,DESTINATION,TYPE)\
##            VALUES('ID1','Name1','Jalandhar','Phagwara','FAST')")

##cursor=conn.execute('Select * from DETAILS')
##names = list(map(lambda x: x[0], cursor.description))
##print(names)

## TO CHECK ALL COLUMNS OF A TABLE ^

root=Tk()
root.geometry("800x400")
root.title("Cour")

def header(window,rows): #Used to add the tabular headers

    f1=Label(window,text="ID",bg="#fc9126")
    f2=Label(window,text="Name",bg="#fc9126")
    f3=Label(window,text="Departing From",bg="#fc9126")
    f4=Label(window,text="Destination",bg="#fc9126")
    f5=Label(window,text="Order Priority",bg="#fc9126")

    f1.config(font=("Helvetica", 20,"bold"))
    f2.config(font=("Helvetica", 20,"bold"))
    f3.config(font=("Helvetica", 20,"bold"))
    f4.config(font=("Helvetica", 20,"bold"))
    f5.config(font=("Helvetica", 20,"bold"))
   
    f1.grid(row=rows,column=0)
    f2.grid(row=rows,column=1)
    f3.grid(row=rows,column=2)
    f4.grid(row=rows,column=3)
    f5.grid(row=rows,column=4)
   
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)

def complete_db(): # View the complete DB

    window=Toplevel(root)
    window.geometry("800x400+600+250")
    window.title("Database")

    table=conn.execute("SELECT * FROM DETAILS")

    header(window,0)
   
    rows=1
    for item in table:
        cols=0
        for i in item:
            new1=Label(window,text=i)
            new1.config(font=("Helvetica", 10,"bold"))
            new1.grid(row=rows,column=cols)
            cols+=1
        rows+=1
       
   
def search_screen(): # Search for an entry using TrackID
    search=input("Enter tracking ID :")
    window=Toplevel(root)
    window.geometry("800x400+600+250")
    window.title("New")
   
    header(window,0)
    query="SELECT * FROM DETAILS WHERE ID='{}'"

    table=conn.execute(query.format(search))
   
    rows=4
    for item in table:
        cols=0
        for i in item:
            new1=Label(window,text=i)
            new1.config(font=("Helvetica", 10,"bold"))
            new1.grid(row=rows,column=cols)
            cols+=1
        rows+=1
       
def add_db(): # Add new entry
   
    a=tuple(map(str,input("Enter").split()))
    query="INSERT INTO DETAILS(ID,NAME,DEPARTURE,DESTINATION,TYPE) VALUES{}"
    table=conn.execute(query.format(a))
   
    rows=1
    for item in table:
        cols=0
        for i in item:
            new1=Label(window,text=i)
            new1.config(font=("Helvetica", 10,"bold"))
            new1.grid(row=rows,column=cols)
            cols+=1
        rows+=1
   
def info(): # Contributors
    window=Toplevel(root)
    window.geometry("800x400+600+250")
    window.title("New")
    window.config(background="#fc9126")
    lab=Label(window,text="\nThis project is developed by -\
    \n\n\nSunshodhan Makkar 11802065 B43\n Akash Kumar Singh \
11802072 B44\nAbhishek Sharma 11802082 B45\nK18GA\nLovely \
Professional University")
    lab.config(font=("Helvetica", 20,"bold"),bg="#fc9126")
    lab.pack(fill=tkinter.X)
   
def close(): # Exit Button
    root.destroy()
   
# Menu
b1=Button(root,text="View all shipments",width=23,height=2,bg="#cfc8c8",command=complete_db)
b2=Button(root,text="Search an order",width=23,height=2,bg="#cfc8c8",command=search_screen)
b3=Button(root,text="Create/Add an order",width=23,height=2,bg="#cfc8c8",command=add_db)
b4=Button(root,text="Info",width=12,height=2,bg="#cfc8c8",command=info)
b5=Button(root,text="Exit",width=12,height=2,bg="#cfc8c8",command=close)
lab=Label(root,text="Courier Management System",bg="#fc9126",pady=35,width=100)

lab.config(font=("Helvetica", 30,"bold"))   # Text styling
b1.config(font=("Helvetica", 10,"bold"))
b2.config(font=("Helvetica", 10,"bold"))
b3.config(font=("Helvetica", 10,"bold"))
b4.config(font=("Helvetica", 10,"bold"))
b5.config(font=("Helvetica", 10,"bold"))

lab.grid(row=0,column=0,columnspan=2)   # Grid
b1.grid(row=2,column=0,pady=5,columnspan=2)
b2.grid(row=3,column=0,pady=5,columnspan=2)
b3.grid(row=4,column=0,pady=5,columnspan=2)
b4.grid(row=5,column=0,pady=5,columnspan=2)
b5.grid(row=6,column=1,padx=20)

root.grid_columnconfigure(0, weight=1)

root.mainloop()
conn.commit()
conn.close()














