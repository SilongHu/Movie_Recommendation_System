#coding:utf-8
import urllib
import re

page = 0
j=0
link = 1
while j<10:
    url = "http://movie.douban.com/top250?start="+str(page)+"&filter=&type="
    content =urllib.urlopen(url).read()
    #抓取电影名
    prenamelocate = 0
    prename = re.compile(r'img alt')
    prenamelist = re.findall(prename,content)
    aftname = re.compile(r'src=')
    aftnamelist = re.findall(aftname,content)
    #抓取电影ID
    preidlocate = 0
    preid = re.compile(r'em class=')
    preidlist = re.findall(preid,content)
    aftid = re.compile(r'img alt')
    aftidlist = re.findall(aftid,content)
    #抓取平均得分
    prescorelocate = 0
    prescore = re.compile(r' \&nbsp')
    prescorelist = re.findall(prescore,content)
    #抓取图片地址
    img = re.compile(r'src="(.+?\.jpg)" class=')
    imglist = re.findall(img,content)
    #抓取电影地址
    premovielocate = 0
    premovie = re.compile(r'em class=')
    premovielist = re.findall(premovie,content)
    aftmovie = re.compile(r'img alt')
    aftmovielist = re.findall(aftmovie,content)
    #抓取每一页的以上数据
    i=0
    while i<25:
        prenamelocate = content.find(prenamelist[0],prenamelocate)
        aftnamelocate = content.find(aftnamelist[0],prenamelocate)
        name = content[prenamelocate+9:aftnamelocate-2]
        print name
        code.open('top250direct.txt','a','utf-8').write(name+'   ')
        prenamelocate = prenamelocate + 7

        preidlocate = content.find(preidlist[0],preidlocate)
        aftidlocate = content.find(aftidlist[0],preidlocate)

        premovielocate = content.find(premovielist[0],premovielocate)
        aftmovielocate = content.find(aftmovielist[0],premovielocate)
        if link/100 != 0:  
            movie_id = content[preidlocate+80+2:aftidlocate-29]
            movie_net = content[premovielocate+48+2:aftmovielocate-28]
        elif link/10 != 0:
            movie_id = content[preidlocate+80+1:aftidlocate-29]
            movie_net = content[premovielocate+48+1:aftmovielocate-28]
        else:
            movie_id = content[preidlocate+80:aftidlocate-29]
            movie_net = content[premovielocate+48:aftmovielocate-28]
        print movie_id
        code.open('top250direct.txt','a','utf-8').write(movie_id+'   ')
        preidlocate = preidlocate + 9
        link+=1

        prescorelocate = content.find(prescorelist[0],prescorelocate)
        score = content[prescorelocate-47:prescorelocate-44]
        print score
        code.open('top250direct.txt','a','utf-8').write(score+'   ')
        prescorelocate = prescorelocate + 10
        
        code.open('top250direct.txt','a','utf-8').write(imglist[i]+'    ')

        code.open('top250direct.txt','a','utf-8').write(movie_net+'    ')
        premovielocate = premovielocate + 9
        #进入电影子网
        subcontent =urllib.urlopen(movie_net).read()
        predir = re.compile(r'directedBy')
        predirlist = re.findall(predir,subcontent)
        aftdir = re.compile(r'</a>')
        aftdirlist = re.findall(aftdir,subcontent)
        predirlocate = subcontent.find(predirlist[0])
        aftdirlocate = subcontent.find(aftdirlist[0],predirlocate)
        director = subcontent[predirlocate+12:aftdirlocate]
        print director
        code.open('top250direct.txt','a','utf-8').write(director+'   ')
    
        #抓取3名主演
        stars = ['']*3
        prestarlocate = 0
        prestar = re.compile(r'starring')
        prestarlist = re.findall(prestar,subcontent)
        aftstar = re.compile(r'</a>')
        aftstarlist = re.findall(aftstar,subcontent)
        k = 0
        while k<3:
            prestarlocate = subcontent.find(prestarlist[0],prestarlocate)
            aftstarlocate = subcontent.find(aftstarlist[0],prestarlocate)
            stars[k] = subcontent[prestarlocate+10:aftstarlocate]
            print stars[k]
            code.open('top250direct.txt','a','utf-8').write(stars[k]+'   ')
            k+=1
            prestarlocate = prestarlocate + 10
        else:
            print "stars over"
        #抓取上映日期
        predate = re.compile(r'initial')
        predatelist = re.findall(predate,subcontent)
        predatelocate = subcontent.find(predatelist[0])
        date = subcontent[predatelocate+29:predatelocate+39]
        print date
        code.open('top250direct.txt','a','utf-8').write(date+'   ')
        #抓取标签
        pretag = re.compile(r'genre')
        afttag = re.compile(r'</span>')
        pretaglist = re.findall(pretag,subcontent)
        afttaglist = re.findall(afttag,subcontent)
        pretaglocate = 0
        tags = ['']*10
        p = 0
        while pretaglocate != -1:
            pretaglocate = pretaglocate + 5
            pretaglocate = subcontent.find(pretaglist[0],pretaglocate)
            afttaglocate = subcontent.find(afttaglist[0],pretaglocate)
            if pretaglocate !=-1:
                tags[p] = subcontent[pretaglocate+7:afttaglocate]
                print tags[p]
                code.open('top250direct.txt','a','utf-8').write(tags[p]+'   ')
            p+=1
        else:
            code.open('top250direct.txt','a','utf-8').write('\n')
            print "tags over"
        print "suburl over"
        i+=1
    else:
        print "found end"
    page = page + 25
    j+=1
else:
    print "top 250 finished!"
