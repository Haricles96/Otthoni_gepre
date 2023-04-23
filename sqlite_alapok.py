'''
Írj egy programot, amely SQLite adatbázisban tárolja ezen fájlban található adatokat!
Az adatokat nem kell feltélenül fájlból beolvasnia a programnak. A program olvassa ki az adatbázisból és listázza ki az adatokat!
'''

import sqlite3
con = sqlite3.connect("nyelvek.db")
cur = con.cursor()
cur.execute("CREATE TABLE nyelv(ev,nyelv,vnev,knev)")

with open("nyelvek.txt", "r", encoding="utf-8") as file:
    for row in file:
        sor = row.strip().split(";")
        data=[(sor[0],sor[1],sor[2],sor[3])]
        cur.executemany("INSERT INTO nyelv VALUES(?,?,?,?)",data)

        con.commit()
        res = cur.execute("SELECT * FROM nyelv")

for row in cur.execute("SELECT * FROM nyelv"):
    print (row)

