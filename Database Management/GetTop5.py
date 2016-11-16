# coding=utf-8
import MySQLdb
import sys
conn = MySQLdb.connect(host ='localhost',user = 'root', passwd = 'husl',db = 'useful',charset = 'utf8')
cur = conn.cursor()
cur.execute("drop table IF EXISTS Top5")
cur.execute("create table Top5(Mid varchar(20),Mname varchar(50),\
    Score float(2), Pictures varchar(100), Websites varchar(100), \
    Directors varchar(50), Performer1 varchar(50),Performer2 varchar(50),\
    Performer3 varchar(50), Year varchar(15),Tag1 varchar(10), Tag2 varchar(10),Tag3 varchar(10),\
    Tag4 varchar(10), Tag5 varchar(10), Tag6 varchar(10))")

cur.execute("SELECT Mid FROM `movie_500` where Year like '2015%'")
Rows = cur.fetchall()
Length = len(Rows)
i = 0
M_S = {}
Top = {}
while i < Length:
    cur.execute("select Score from movie_500 where Mid = '%s' " %Rows[i])
    score = cur.fetchall()
    #Year.append(Rows[i][0][0:4])
    x = {Rows[i]:score}
    M_S.update(x)
    #print M_S
    i = i + 1
#print M_S
M_S = sorted(M_S.items(), key=lambda M_S:M_S[1])
Top = M_S[-5:]

j = 0
while j<5:
    cur.execute("select * from movie_500 where Mid = '%s' " %(Top[j][0][0]))
    detail = cur.fetchall()
    cur.execute("insert into Top5 set Mid='%s'" %(detail[0][0]))
    cur.execute("update Top5 set Mname = '%s' where Mid='%s' " %(detail[0][1],detail[0][0]))
    cur.execute("update Top5 set Score = '%s' where Mid='%s' " %(detail[0][2],detail[0][0]))
    cur.execute("update Top5 set Pictures = '%s' where Mid='%s' " %(detail[0][3],detail[0][0]))
    cur.execute("update Top5 set Websites = '%s' where Mid='%s' " %(detail[0][4],detail[0][0]))
    cur.execute("update Top5 set Directors = '%s' where Mid='%s' " %(detail[0][5],detail[0][0]))
    cur.execute("update Top5 set Performer1 = '%s' where Mid='%s' " %(detail[0][6],detail[0][0]))
    cur.execute("update Top5 set Performer2 = '%s' where Mid='%s' " %(detail[0][7],detail[0][0]))
    cur.execute("update Top5 set Performer3 = '%s' where Mid='%s' " %(detail[0][8],detail[0][0]))
    cur.execute("update Top5 set Year = '%s' where Mid='%s' " %(detail[0][9],detail[0][0]))
    cur.execute("update Top5 set Tag1 = '%s' where Mid='%s' " %(detail[0][10],detail[0][0]))
    cur.execute("update Top5 set Tag2 = '%s' where Mid='%s' " %(detail[0][11],detail[0][0]))
    cur.execute("update Top5 set Tag3 = '%s' where Mid='%s' " %(detail[0][12],detail[0][0]))
    cur.execute("update Top5 set Tag4 = '%s' where Mid='%s' " %(detail[0][13],detail[0][0]))
    cur.execute("update Top5 set Tag5 = '%s' where Mid='%s' " %(detail[0][14],detail[0][0]))
    cur.execute("update Top5 set Tag6 = '%s' where Mid='%s' " %(detail[0][15],detail[0][0]))
    print j , 'movie ok'
    j= j+ 1

cur.close()
conn.commit()
conn.close()
