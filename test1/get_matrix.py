#encoding=utf-8
# 来源：整理总结
import MySQLdb as mdb
import sys
import numpy as np

def GetMatrix(Table):
    #连接mysql，获取连接的对象
    con = mdb.connect(host='localhost', user='root', passwd='13911899858', db='python',charset='utf8');
    with con:
        #仍然是，第一步要获取连接的cursor对象，用于执行查询
        cur = con.cursor()
        cur.execute("SELECT * FROM %s "%Table)#user_movie
        rows=cur.fetchall()
        a=len(rows[0])
        b=len(rows)
        print a
        print b
        """
        desc = cur.description

        a=len(desc)
        print a
        #打印表头，就是字段名字
        mid=[]
        for i in range(1,a):
            mid.append(desc[i][0])
        #print mid

        b=len(rows)
        print b
        uid=[]
        
        for i in range(b):
            uid.append(rows[i][0])
        #print uid
        """
        matrix = np.zeros((b,a-1))

        for i in range(b):
            for j in range(1,a):
                if(rows[i][j]!=None):
                    matrix[i][j-1]=rows[i][j]
        #print matrix[677][211]
    cur.close()
    con.commit()
    con.close()
    return matrix

if __name__ == "__main__":
    table='user_movie'
    Matrix=GetMatrix(table)
    print "matrix:"
    print Matrix.shape[0]
    print Matrix.shape[1]
