# coding=utf-8
import MySQLdb
import sys
conn = MySQLdb.connect(host ='localhost',user = 'root', passwd = 'husl',db = 'useful',charset = 'utf8')
cur = conn.cursor()
cur.execute("drop table IF EXISTS Movie_Tag")
cur.execute("create table Movie_Tag(Mid varchar(20))")


fin = open(r'movie500.txt', 'r')                               
k = 0
Elements_U = {}
Row_Elements = {}
MovieID = []
Tags = []
for line in fin:
    Elements_U[k] =  line.split('\t')
    n = len(Elements_U[k])   #1 for id , 5 for director, 10.. for tags
    Row_Elements[k] = ['M'+Elements_U[k][1]]
    t = 10 
    MovieID.append('M'+Elements_U[k][1])
    while t < n-1:
        Tags.append(Elements_U[k][t])
        Row_Elements[k].append(Elements_U[k][t])
        t = t + 1
    print k , 'movie ok'
    k = k + 1
Length = len(Elements_U)
Movie_Len = len(MovieID)
Tags_NR = sorted(set(Tags),key = Tags.index)
Tags_Len = len(Tags_NR)
Tag_Eng = ['story','crime','action','love','homosexual','war','music','cartoon','fantasy', 'comedy','fiction','advanture',
        'disaster', 'suspense','opera', 'child', 'family' ,'biography','document' ,'ancient', 'stuned','history','horrible', 'west', 'porn', 'kingfu', 'sports']

m = 0
n = 0
while m < Movie_Len:
    cur.execute("insert into Movie_Tag set Mid = '%s'" %(MovieID[m]))
    m = m + 1
while n < Tags_Len:
    cur.execute("alter table Movie_Tag add column %s int(2)" %(Tags_NR[n]))
    n = n + 1
p = 0
while p < Length:   #Movie-Tag data insert
    w = len(Row_Elements[p])
    q = 1
    while q < w:
        cur.execute("update Movie_Tag set %s = '1' where Mid = '%s'" %(Row_Elements[p][q],Row_Elements[p][0]))
        q = q + 1
        
    cur.execute("select * from Movie_Tag where Mid= '%s' " %(Row_Elements[p][0]))
    detail = cur.fetchall()
    print detail
    l = 1
    while l<28:
        if (detail[0][l]== None):
            cur.execute("update Movie_Tag set %s = '0' where Mid = '%s'" %(Tags_NR[l-1],Row_Elements[p][0]))
        l = l + 1
            
    p = p + 1
    print p, 'movie insert success'
cur.close()
conn.commit()
conn.close()
