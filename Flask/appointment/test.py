import sqlite3
conn=sqlite3.connect("../site.db")
print("Opened database successfully")
cursor=conn.execute("SELECT * FROM user WHERE id=1")
for i in cursor:
    print ("id = ",i[0],i[1],i[2],i[3],i[4])