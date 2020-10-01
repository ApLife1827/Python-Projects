import sqlite3 
conn = sqlite3.connect('pakdet.db')
c2 = conn.cursor() 
#c2.execute("""CREATE TABLE PAKDET(REG text,BLOCK text,VEHICLE text)""")
for row in c2.execute("SELECT * FROM PAKDET"):
    print(row)
conn.close()  
