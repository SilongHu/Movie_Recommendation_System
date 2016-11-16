#coding=utf-8
import MySQLdb
import sys
conn = MySQLdb.connect(host ='localhost',user = 'root', passwd = 'husl',db = 'useful',charset = 'utf8')
cur = conn.cursor()

cur.execute("drop table IF EXISTS User_PS")
cur.execute("create table User_PS(Uid varchar(20),Password varchar(20))")

cur.execute("select * from User_Movie")
Rows = cur.fetchall()
Length = len(Rows)
i = 0

User = []
print Rows[1][0]
while i < Length:
    User.append(Rows[i][0])
    i = i + 1  

n = 0
while n < Length:
    cur.execute("insert into User_PS set Uid = '%s'" %(User[n]))
    cur.execute("update User_PS set Password = %s where Uid = '%s'" %(1111,User[n]))
    n = n + 1
    print n,'User insert success'

cur.close()
conn.commit()
conn.close()
