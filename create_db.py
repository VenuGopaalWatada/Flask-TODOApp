import sqlite3 as sql

con =  sql.connect('data.db')

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS Tasks")

comm = '''CREATE TABLE "Tasks" ( 
          "TID" INTEGER PRIMARY KEY AUTOINCREMENT, 
          "DESCRIPTION" TEXT
        )'''
        
cur.execute(comm)

con.commit()

con.close()