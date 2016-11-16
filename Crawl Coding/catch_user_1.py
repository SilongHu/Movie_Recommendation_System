import urllib2
import time
import re
import sys
#import main
#headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
#req1 = urllib2.Request("",headers=headers)
#con = urllib2.urlopen(req1).read()
def function(net):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0' }
    url1 = 'http://movie.douban.com/people/'+str(net)+'/reviews?'
    req1 = urllib2.Request(url1,headers=headers)
    con1 = urllib2.urlopen(req1).read()

    findNumber = "\\(\d{1,3}\\)"
    endofline = re.compile(findNumber)
    endd = re.findall(endofline,con1)
    x_number_s = con1.find(endd[0])
    x_number_end = con1.find('</title>')
    x1 = con1[x_number_s+1:x_number_end-2]
    x = int(x1)
    page = 0
    usernet = ['']*x
    username = ['']*x
    movieid = ['']*x
    moviename = ['']*x
    moviestar = ['']*x
    message = ['']*x
    link = 1
    while page <=(x)/10:
        
        url = 'http://movie.douban.com/people/'+str(net)+'/reviews?start='+str(page*10)
        req = urllib2.Request(url,headers=headers)
        con = urllib2.urlopen(req).read()
        i = 0
        user_name_start = con.find(r'starb')
        user_name_usernet = con.find(r'href=',user_name_start)
        user_name_usernetend = con.find(r'">',user_name_usernet)
        user_name_end = con.find(r'</a',user_name_usernetend)
        movie_id = con.find(r'href=',user_name_end)
        movie_id_end = con.find(r'">',movie_id)
        movie_name_end = con.find(r'</a',movie_id_end)
        movie_star = con.find(r'allstar')
        while i < x and user_name_start != -1:
            usernet[i] = con[user_name_usernet+6:user_name_usernetend]
            username[i] = con[user_name_usernetend+2:user_name_end]
            movieid[i] = con[movie_id+38:movie_id_end-1]
            moviename[i] = con[movie_id_end+3:movie_name_end]
            moviestar[i] = con[movie_star+7:movie_star+8]
            message[i] = usernet[i]+' '+str(net)+' '+movieid[i]+' '+moviestar[i]
            print link,' ',message[i]
            f = open(r'user_name_4.txt','a')
            f.write(message[i])
            f.write("\n")
            user_name_start = con.find(r'starb',movie_star)
            user_name_usernet = con.find(r'href=',user_name_start)
            user_name_usernetend = con.find(r'">',user_name_usernet)
            user_name_end = con.find(r'</a',user_name_usernetend)
            movie_id = con.find(r'href=',user_name_end)
            movie_id_end = con.find(r'">',movie_id)
            movie_name_end = con.find(r'</a',movie_id_end)
            movie_star = con.find(r'allstar',movie_name_end)
            i = i + 1
            link = link + 1
        else:
            print page+1,'download finish'
            page = page + 1
            time.sleep(1)
    else:
        print all,'find end'

    


