#encoding=utf-8
# 来源：整理总结
import MySQLdb as mdb
import sys
import numpy as np
from scipy.sparse.linalg import svds  
from scipy import sparse
import get_matrix
def vector_to_diagonal(vector):  
    """
    将向量放在对角矩阵的对角线上
    :param vector:
    :return:
    """
    if (isinstance(vector, np.ndarray) and vector.ndim == 1) or \
            isinstance(vector, list):
        length = len(vector)
        diag_matrix = np.zeros((length, length))
        np.fill_diagonal(diag_matrix, vector)
        return diag_matrix
    return None

def svd_update():
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


    RATE_MATRIX = get_matrix.GetMatrix('user_movie')
    RATE_MATRIX = RATE_MATRIX.astype('float')  
    U, S, VT = svds(sparse.csr_matrix(RATE_MATRIX),  k=5, maxiter=200) # 5个隐主题  
    S = vector_to_diagonal(S)
    """
    print '用户的主题分布：'  
    print U  
    print '奇异值：'  
    print S  
    print '物品的主题分布：'  
    print VT  
    print '重建评分矩阵，并过滤掉已经评分的物品：'
    """
    result = np.dot(np.dot(U, S), VT) * (RATE_MATRIX < 1e-6)
    #print result

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
    
    for line in range(b):
            cur.execute("update recommendation set s1 = '%s' where Uid='%s' " %(recommendation[line][0],uid[line]))
            cur.execute("update recommendation set s2 = '%s' where Uid='%s' " %(recommendation[line][1],uid[line]))
            cur.execute("update recommendation set s3 = '%s' where Uid='%s' " %(recommendation[line][2],uid[line]))
            print line , 'user ok'

    cur.close()
    con.commit()
    con.close()

if __name__ == "__main__":
                        
    svd_update()

