import sqlite3
conn=sqlite3.connect('test1.db')
c=conn.cursor()
#c.execute("""CREATE TABLE STUDENT(Name text,Regno text,Gender text, Mobile text,Email text,Username text,Password text)""")
#c.execute("INSERT INTO PARK values('Gourab',11503537,'Male','8946065442','gourab19964u@gmail.com','gourab19964u','12345678')")
for row in c.execute('SELECT * FROM PARK'):
        print(row)
conn.commit()
conn.close()

