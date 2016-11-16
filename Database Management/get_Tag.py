#encoding=utf-8
# 来源：整理总结
import MySQLdb as mdb
import sys

#def user_bayes(UserID,Input_movie):
    
    #native_bayes(data,test,c_name,c_value)
    
def p(data,c_name,c_value):#类别先验概率
    count = 0.0
    for e in data:
        if e[c_name] == c_value:
            count += 1
    #print(count/len(data))            
    return count/len(data)

def pp(data,c_name,c_value,a_name,a_value):#属性先验概率
    count1 = 0.0
    count2 = 0.0
    for e in data:
        if e[c_name] == c_value:
            count1 += 1
            if e[a_name] == a_value:
                count2 += 1
    return count2/count1

def native_bayes(UserID,Input_movie):#贝叶斯公式计算后验概率
    con = mdb.connect(host='localhost', user='root', passwd='husl', db='useful',charset='utf8');
    with con:
        #仍然是，第一步要获取连接的cursor对象，用于执行查询
        cur = con.cursor()
        cur.execute("SELECT * FROM movie_Tag")
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
        #print uid
    
        dict1={}
        for i in range(b):
            dict1[uid[i]]={}
            for j in range(1,a):
                dict1[uid[i]][mid[j-1]]=rows[i][j]
    #dict1['M1292052']['score']=4
    #print dict1['M1292052']
        cur.execute("select * from user_movie where Uid = '%s' " %(UserID))
        detail = cur.fetchall()
        if detail !=():
            Seen_Score = []
            Mark = []
            Movie_Seen = []
            i = 1
            while i< 500:
                if detail[0][i] != None:
                    Seen_Score.append(detail[0][i])
                    Mark.append(i)
                i = i + 1            
            Mark_Len = len(Mark)
            cur.execute("select Mid from movie_item")
            movie = cur.fetchall()
            j = 0
            while j < Mark_Len:
                Movie_Seen.append(movie[Mark[j]-1])
                j = j + 1
        else:
            print 'user does not exist'
        Seen_Score_NR = sorted(set(Seen_Score),key = Seen_Score.index)
        Record = {}
        
        Movie_Len = len(Movie_Seen)
        k = 0
        a = []
        data = []
        while k < Movie_Len:      
            cur.execute("select * from Movie_Tag where Mid = '%s' " %(Movie_Seen[k]))
            haha = cur.fetchall()      
            a.append(haha[0][0])
            Record[UserID,k]=dict1[a[k]]
            Record[UserID,k]['score'] = Seen_Score[k]
            data.append(Record[UserID,k])
            k= k + 1
        data.append({'\xe7\x8a\xaf\xe7\xbd\xaa': 0L,'\xe5\x8a\xa8\xe4\xbd\x9c': 0L,
    '\xe6\x83\x8a\xe6\x82\x9a': 0L,'\xe5\xae\xb6\xe5\xba\xad': 0L,
    '\xe5\x89\xa7\xe6\x83\x85': 0L,'\xe9\x9f\xb3\xe4\xb9\x90': 0L,
    '\xe6\xad\xa6\xe4\xbe\xa0': 0L, '\xe8\xbf\x90\xe5\x8a\xa8': 0L,
    '\xe6\x88\x98\xe4\xba\x89': 0L, '\xe4\xbc\xa0\xe8\xae\xb0': 0L,
    '\xe5\x8e\x86\xe5\x8f\xb2': 0L, '\xe6\x83\x85\xe8\x89\xb2': 0L,
    '\xe5\x84\xbf\xe7\xab\xa5': 0L, '\xe6\x82\xac\xe7\x96\x91': 0L,
    '\xe7\x81\xbe\xe9\x9a\xbe': 0L, '\xe7\x88\xb1\xe6\x83\x85': 0L,
    '\xe7\xba\xaa\xe5\xbd\x95\xe7\x89\x87': 0L, '\xe5\x86\x92\xe9\x99\xa9': 0L,
    '\xe5\xa5\x87\xe5\xb9\xbb': 0L, '\xe7\xa7\x91\xe5\xb9\xbb': 0L,
    '\xe5\x8f\xa4\xe8\xa3\x85': 0L, '\xe6\xad\x8c\xe8\x88\x9e': 0L,
    '\xe6\x81\x90\xe6\x80\x96': 0L, '\xe5\x96\x9c\xe5\x89\xa7': 0L,
    '\xe5\x8a\xa8\xe7\x94\xbb': 0L, '\xe5\x90\x8c\xe6\x80\xa7': 0L,
    '\xe8\xa5\xbf\xe9\x83\xa8': 0L,'score':0.0})
        
    cur.close()
    con.commit()
    con.close()
    c_name = 'score'
    Seen_Score_NR.append(0.0)
    c_value = Seen_Score_NR
    #Input_movie = 'M1292001'
    #ur.execute("select * from Movie_Tag where Mid = '%s' " %(Input_movie))
    test = dict1[Input_movie]
    pv = [0]*len(c_value)
    '''
    for value in c_value:
        print(c_value.index(value))
        pv[c_value.index(value)] = p(data,c_name,value)
    '''
    for i in range(len(c_value)):
        pv[i] = p(data,c_name,c_value[i])
    '''
    for value in c_value:
        for a_name,a_value in test.items():
            pv[c_value.index(value)] = pv[c_value.index(value)]*pp(data,c_name,value,a_name,a_value)
    '''
    
    for i in range(len(c_value)):
        for a_name,a_value in test.items():
            pv[i] = pv[i]*pp(data,c_name,c_value[i],a_name,a_value)
    
    print("目标样本类别归属为：%s" %(c_value[pv.index(max(pv))]))
    return c_value[pv.index(max(pv))]
    

native_bayes('CyberKnight','M2131459')

#a = native_bayes('CyberKnight','M2131459')
#print a
   
