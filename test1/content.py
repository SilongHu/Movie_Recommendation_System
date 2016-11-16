import MySQLdb as mdb
import numpy as np
import scipy as sp
import numpy
import math
import get_matrix
def ContentBased(M_T,U_M):
    Row_M = M_T.shape[0] #M-T matrix row number, means movieID number
    Column_M = M_T.shape[1]#Tags + Directors number
    Row_U = U_M.shape[0] # User Number
    Column_U = U_M.shape[1] # Movie Number
    User_Scores = [] # Save the user's avr score
    User_Seens = [] #Save the Num of movies every user seen
    U_T = np.zeros((Row_U,Column_M))
    Cos = np.zeros((Row_U,Row_M))
    i = 0
    while i < Row_U: #2
        Num_0 = float((U_M[i].tolist()).count(0)) #count the Num of 0 in user
        User_Seens.append(float(Column_U) - Num_0)
        if Column_U - Num_0 == 0:
            User_Scores.append(0)
        else:
            User_Scores.append(float(sum(U_M[i]))/(Column_U - Num_0))
        k = 0
        while k < Column_M: # 6
            Sum = float(sum(U_M[i] * M_T[:,k]))
            g = 0
            Count_0 = 0
            while g < Row_M: #3
                if U_M[i][g] != 0 and M_T[:,k][g] != 0:
                    Count_0 = Count_0 + 1
                g= g + 1
            if Count_0 ==0:
                U_T[i][k] =0
            else:
                U_T[i][k] = (Sum -User_Scores[i]*Count_0)/Count_0
            k = k + 1
        i = i + 1
    #print  U_T
    
    #Generating the Cos-Sim matrix(2*3)2*6 6*3
    p = 0
    while p < Row_U:
        q = 0
        while q < Row_M:
            count  = (sum(np.square(U_T[p]))*sum(np.square(M_T[q])))**0.5
            if count ==0:
                Cos[p][q] = 0
            else:
                Cos[p][q] = np.dot(U_T[p],M_T[q])/count
            q = q + 1
        p = p + 1
    return Cos * (Cos < 1e-6)
def content_update():
    #连接mysql，获取连接的对象
    con = mdb.connect(host='localhost', user='root', passwd='13911899858', db='python',charset='utf8');

    with con:
        #仍然是，第一步要获取连接的cursor对象，用于执行查询
        cur = con.cursor()
        cur.execute("SELECT * FROM user_movie")
        rows=cur.fetchall()
        desc = cur.description

        a=len(desc)
        mid=[]
        for i in range(1,a):
            mid.append(desc[i][0])

        b=len(rows)
        uid=[]
        for i in range(b):
            uid.append(rows[i][0])        


    R = get_matrix.GetMatrix('user_movie')
    U_M = numpy.array(R)
    print U_M.shape[0]
    print U_M.shape[1]
      
    G = get_matrix.GetMatrix('movie_item')
    M_T = numpy.array(G)
    print M_T.shape[0]
    print M_T.shape[1]
    result = ContentBased(M_T,U_M)

    ROW=result.shape[0]
    COLUMN=result.shape[1]

    dict1={}
    record=[[0]*3 for row in range(ROW)]
    recommendation=[['']*3 for row in range(ROW)]
    for i in range(b):
        for j in range(0,a-1):
            if(result[i][j]!=0):
                dict1[mid[j]]=result[i][j]
        rankings=[(mark,item)for item,mark in dict1.items() ]
        rankings.sort()
        rankings.reverse()
        ranking=rankings[0:3]
        for k in range(3):
            recommendation[i][k]=ranking[k][1]
            record[i][k]=ranking[k][0]
        print recommendation[i]
        
    #print recommendation[0:5]
    #print record[0:5]


    for line in range(b):
        cur.execute("update recommendation set c1 = '%s' where Uid='%s' " %(recommendation[line][0],uid[line]))
        cur.execute("update recommendation set c2 = '%s' where Uid='%s' " %(recommendation[line][1],uid[line]))
        cur.execute("update recommendation set c3 = '%s' where Uid='%s' " %(recommendation[line][2],uid[line]))
        print line , 'user ok'   


    cur.close()
    con.commit()
    con.close()

if __name__ == "__main__":
                        
    content_update()
