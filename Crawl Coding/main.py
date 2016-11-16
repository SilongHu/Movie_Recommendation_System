import urllib2
import time
import re
import sys
import catch_user_1
count = 440
while count<=800:
    headers={"Accept": "*/*","Referer": "http://answers.yahoo.com/","User-Agent": "Mozilla/5.0+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)"}  
    #headers = {'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/4.0.0'}
    url = 'http://movie.douban.com/subject/1291583/comments?start='+str(count)+'&limit=20&sort=new_score'
    req = urllib2.Request(url, headers=headers)


    content = urllib2.urlopen(req).read()
    net = ['']*20
    i = 0
    net_start = content.find(r'comment-info')
    net_started = content.find(r'href=',net_start)
    net_end = content.find(r'class',net_started)
    while i<20:
        net[i] = content[net_started+37:net_end-3]
        print net[i]
        net_start = content.find(r'comment-info',net_end)
        net_started = content.find(r'href=',net_start)
        net_end = content.find(r'class',net_started)    
        i = i + 1
    else:
        print 'finish'
    
    j = 0
    while j<20:
        catch_user_1.function(net[j])
        time.sleep(2)
        j = j + 1
    else:
        print count,'download over'

    count = count + 40


