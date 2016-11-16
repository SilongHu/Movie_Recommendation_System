# coding=utf-8
import MySQLdb
import sys
conn = MySQLdb.connect(host ='localhost',user = 'root', passwd = 'husl',db = 'useful',charset = 'utf8')
cur = conn.cursor()
cur.execute("drop table IF EXISTS Movie_500")
cur.execute("create table Movie_500(Mid varchar(20),Mname varchar(50),\
    Score float(2), Pictures varchar(100), Websites varchar(100), \
    Directors varchar(50), Performer1 varchar(50),Performer2 varchar(50),\
    Performer3 varchar(50), Year varchar(15),Tag1 varchar(10), Tag2 varchar(10),Tag3 varchar(10),\
    Tag4 varchar(10), Tag5 varchar(10), Tag6 varchar(10))")


fin = open(r'movie500.txt', 'r')                               
k = 0
Elements_U = {}
for line in fin:
    Elements_U[k] =  line.split('\t')
    n = len(Elements_U[k])   #1 for id , 5 for director, 10.. for tags
    i = 10
    cur.execute("insert into Movie_500 set Mid='%s'" %('M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Mname = '%s' where Mid='%s' " %(Elements_U[k][0],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Score = '%s' where Mid='%s' " %(Elements_U[k][2],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Pictures = '%s' where Mid='%s' " %(Elements_U[k][3],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Websites = '%s' where Mid='%s' " %(Elements_U[k][4],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Directors = '%s' where Mid='%s' " %(Elements_U[k][5],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Performer1 = '%s' where Mid='%s' " %(Elements_U[k][6],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Performer2 = '%s' where Mid='%s' " %(Elements_U[k][7],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Performer3 = '%s' where Mid='%s' " %(Elements_U[k][8],'M'+Elements_U[k][1]))
    cur.execute("update Movie_500 set Year = '%s' where Mid='%s' " %(Elements_U[k][9],'M'+Elements_U[k][1]))
    while i < n-1:
        cur.execute("update Movie_500 set %s = '%s' where Mid='%s' " %('Tag'+str(i-9),Elements_U[k][i],'M'+Elements_U[k][1]))
        i = i + 1
    print k , 'movie ok'
    k = k + 1

    
cur.close()
conn.commit()
conn.close()
