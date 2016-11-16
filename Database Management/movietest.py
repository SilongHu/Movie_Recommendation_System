# coding=utf-8
import MySQLdb
import sys
conn = MySQLdb.connect(host ='localhost',user = 'root', passwd = 'husl',db = 'useful',charset = 'utf8')
cur = conn.cursor()
cur.execute("drop table IF EXISTS Movie_Item")
cur.execute("create table Movie_Item(Mid varchar(20))")
cur.execute("drop table IF EXISTS User_Movie")      # if the table is not exist
cur.execute("create table User_Movie(Uid varchar(20)) ")
cur.execute("drop table IF EXISTS UM_Verify")      # if the table is not exist
cur.execute("create table UM_Verify(Uid varchar(20)) ")
fin = open(r'movie500.txt', 'r')                                #以读的方式打开输入文件
i = 0
k = 0
Elements = {}
Row_Elements = {}
Directors = []
MovieID = []
Tags = []
for line in fin:
    Elements[i] =  line.split('\t')
    n = len(Elements[i])
    #print n      #1 for id , 5 for director, 10.. for tags
    k = 10
    Row_Elements[i] = ['M'+Elements[i][1],Elements[i][5],Elements[i][9]]
    Directors.append(Elements[i][5])
    while k < n-1:
        Row_Elements[i].append(Elements[i][k])
        k = k + 1
    MovieID.append('M'+Elements[i][1])
    t = 10
    while t < n-1:
        Tags.append(Elements[i][t])
        t = t + 1
    i = i + 1

Length = len(Row_Elements)
Movie_Len = len(MovieID)
Tags_NR = sorted(set(Tags),key = Tags.index)

Tags_Len = len(Tags_NR)
Directors_NR =sorted(set(Directors),key = Directors.index)
#print Directors_NR
Director_Len = len(Directors_NR)

m = 0
n = 0
g = 0
while m < Movie_Len:
    cur.execute("insert into Movie_Item set Mid = '%s'" %(MovieID[m]))
    cur.execute("alter table User_Movie add column %s float(2) "%(MovieID[m]))
    cur.execute("alter table UM_Verify add column %s float(2) "%(MovieID[m]))
    m = m + 1
    #print m, 'MovieID insert success'
    
while n < Tags_Len:
    cur.execute("alter table Movie_Item add column %s int(2)" %(Tags_NR[n]))
    n = n + 1
    print n , 'Tags insert success'
    
while g < Director_Len:
    cur.execute("alter table Movie_Item add column %s int(2)" %(Directors_NR[g]))
    g = g + 1
    #print g , 'Directors insert success'
    

p = 0
while p < Length:   #Movie-Item data insert
    cur.execute("update Movie_Item set %s = '1' where Mid = '%s'" %(Row_Elements[p][1], Row_Elements[p][0]))
    w = len(Row_Elements[p])
    q = 3
    while q < w:
        cur.execute("update Movie_Item set %s = '1' where Mid = '%s'" %(Row_Elements[p][q],Row_Elements[p][0]))
        q = q + 1
    p = p + 1
    print p, 'movie insert success'

#dealing with the User-Movie chart
fin1 = open(r'hsl.txt', 'r')                                #以读的方式打开输入文件
ii = 0
kk = 0 
Elements_U = {}
Row_Elements_U = {}
UserID = []
Score = []
for lines in fin1:
    Elements_U[ii] =  lines.split()
    if ((Elements_U[ii][3]) != 'N'):
        Row_Elements_U[ii] = [Elements_U[ii][1],Elements_U[ii][2],Elements_U[ii][3]]
        if ii>0 and (Row_Elements_U[ii][0] != Row_Elements_U[ii-1][0]):
            UserID.append(Row_Elements_U[ii][0])
    else:
        continue
    ii = ii + 1     
length1 = len(Row_Elements_U)   
UserID.insert(0,Row_Elements_U[0][0])
print len(UserID)
#UserID_NR = sorted(set(UserID),key = UserID.index)
#ID_Len = len(UserID_NR)

'''m1 = 0
n1 = 0
while m1 < ID_Len:
    #count = cur.execute("select 1 from User_Movie where Uid ='%s' limit 1" %(UserID_NR[m]))
    #if count ==0 :
    cur.execute("insert into User_Movie set Uid='%s'" %(UserID_NR[m1]))
    m1 = m1 + 1
    print m1,'User insert success'
    '''

##insert the data into table User_Movie
k1 = 0
while k1 < length1:
    if ('M'+Row_Elements_U[k1][1]) in MovieID:
        if (cur.execute("select * from User_Movie where Uid='%s'" %(Row_Elements_U[k1][0])) == 0):
            cur.execute("insert into User_Movie set Uid='%s'" %(Row_Elements_U[k1][0]))
            cur.execute("update User_Movie set %s = '%s' where Uid='%s' " %('M'+Row_Elements_U[k1][1],float(Row_Elements_U[k1][2]),Row_Elements_U[k1][0]))    
        else:
            cur.execute("update User_Movie set %s = '%s' where Uid='%s' " %('M'+Row_Elements_U[k1][1],float(Row_Elements_U[k1][2]),Row_Elements_U[k1][0]))    
        print k1, 'user insert success'

        if (cur.execute("select * from UM_Verify where Uid='%s'" %(Row_Elements_U[k1][0])) == 0):
            cur.execute("insert into UM_Verify set Uid='%s'" %(Row_Elements_U[k1][0]))
            cur.execute("update UM_Verify set %s = '%s' where Uid='%s' " %('M'+Row_Elements_U[k1][1],1,Row_Elements_U[k1][0]))    
        else:
            cur.execute("update UM_Verify set %s = '%s' where Uid='%s' " %('M'+Row_Elements_U[k1][1],1,Row_Elements_U[k1][0]))    
        print k1, 'user verify success'
    k1 = k1 + 1
        
cur.close()
conn.commit()
conn.close()

