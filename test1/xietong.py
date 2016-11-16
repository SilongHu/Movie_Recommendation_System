#encoding=utf-8
# 来源：整理总结
import MySQLdb as mdb
import sys
from math import sqrt

#计算pearson系数
def sim_pearson(prefs, p1, p2):
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item] = 1
	n = len(si)
	if n == 0: return 1
	sum1 =  sum([prefs[p1][it] for it in si] )
	sum2 =  sum([prefs[p2][it] for it in si] )

	sum1sq = sum([pow(prefs[p1][it], 2) for it in si])
	sum2sq = sum([pow(prefs[p2][it], 2) for it in si])

	psum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

	num = psum - (sum1 * sum2 / n)
	den = sqrt((sum1sq - pow(sum1, 2) / n ) * (sum2sq - pow (sum2, 2) / n))
	if den == 0: return 0
	r = num/den
	return r
    
#获取推荐列表
def  getRecommendations(prefs, person, similarity=sim_pearson):
	totals={}
	simSum={}
	for other in prefs:
		if other == person: continue
		sim = similarity(prefs, person, other)

		if sim <= 0: continue
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item, 0)
				totals[item] += prefs[other][item] * sim
				simSum.setdefault(item, 0)
				simSum[item] += sim

	rankings = [(total/simSum[item],item)for item,total in totals.items() ]

	rankings.sort()
	rankings.reverse()
	return rankings
    
#对所有用户推荐进行更新
def xietong_update():
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
        #print uid
        
        dict1={}
        for i in range(b):
            dict1[uid[i]]={}
            for j in range(1,a):
                if(rows[i][j]!=0 and rows[i][j]!=None):
                    dict1[uid[i]][mid[j-1]]=rows[i][j]
                    
        recommendation=[['']*3 for row in range(b)]            
        for u in range(b):
            ranking=getRecommendations(dict1, uid[u])
            for i in range(3):
                recommendation[u][i]=ranking[i][1]
            print recommendation[u]
        
        for line in range(b):
            cur.execute("update recommendation set x1 = '%s' where Uid='%s' " %(recommendation[line][0],uid[line]))
            cur.execute("update recommendation set x2 = '%s' where Uid='%s' " %(recommendation[line][1],uid[line]))
            cur.execute("update recommendation set x3 = '%s' where Uid='%s' " %(recommendation[line][2],uid[line]))
            print line , 'user ok'
        
    cur.close()
    con.commit()
    con.close()

    #return recommendation                        

if __name__ == "__main__":
    xietong_update()                    
    

