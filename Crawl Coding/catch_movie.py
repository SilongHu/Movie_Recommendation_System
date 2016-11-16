#coding:utf-8
import urllib
import re
#在用户数据中找到电影ID并检查电影ID库中是否已存在
idd = re.compile(r' (\d+) '
user = open("user.txt",'r')
for line in user:
    iddlist = re.findall(idd,line)
    print iddlist[0]
    url = "http://movie.douban.com/subject/"+str(iddlist[0])+"/"
    content =urllib.urlopen(url).read()
    flag = 0

    fo = open("movie_id.txt",'r')
    for ids in fo:
        if ids == iddlist[0]+"\n":
            flag = 1
            print "already have!"
            break;
        else:
            continue
    #如果电影不存在则添加该电影的信息至电影库
    if flag == 0:
        prename = re.compile(r'itemre')
        prenamelist = re.findall(prename,content)
        aftname = re.compile(r'</span>')
        aftnamelist = re.findall(aftname,content)
        prenamelocate = content.find(prenamelist[0])
        aftnamelocate = content.find(aftnamelist[0],prenamelocate)
        name = content[prenamelocate+14:aftnamelocate]

        prescore = re.compile(r'average')
        prescorelist = re.findall(prescore,content)
        prescorelocate = content.find(prescorelist[0])
        score = content[prescorelocate+9:prescorelocate+12]

        img = re.compile(r'src="(.+?\.jpg)" title=')
        imglist = re.findall(img,content)

        movie = "http://movie.douban.com/subject/"+str(iddlist[0])+"/"

        predir = re.compile(r'directedBy')
        predirlist = re.findall(predir,content)
        aftdir = re.compile(r'</a>')
        aftdirlist = re.findall(aftdir,content)
        predirlocate = content.find(predirlist[0])
        aftdirlocate = content.find(aftdirlist[0],predirlocate)
        director = content[predirlocate+12:aftdirlocate]

        if prenamelocate != -1 and aftnamelocate != -1 and prescorelocate != -1 and predirlocate != -1:
            open('movie_id.txt','a').write(iddlist[0]+"\n")
            open('movielist.txt','a').write(name+'   '+iddlist[0]+'   '+score+'   '+imglist[0]+'    '+movie+'    '+director+'   ')
            print name,score,director

            stars = ['']*3
            prestarlocate = 0
            prestar = re.compile(r'starring')
            prestarlist = re.findall(prestar,content)
            aftstar = re.compile(r'</a>')
            aftstarlist = re.findall(aftstar,content)
            k = 0
            while k<3:
                prestarlocate = content.find(prestarlist[0],prestarlocate)
                aftstarlocate = content.find(aftstarlist[0],prestarlocate)
                stars[k] = content[prestarlocate+10:aftstarlocate]
                if prestarlocate != -1 and aftstarlocate != -1:
                    print stars[k]
                    open('movielist.txt','a').write(stars[k]+'   ')
                k+=1
                prestarlocate = prestarlocate + 10
            else:
                print "stars over"

            predate = re.compile(r'initial')
            predatelist = re.findall(predate,content)
            predatelocate = content.find(predatelist[0])
            date = content[predatelocate+29:predatelocate+39]
            if predatelocate != -1:
                print date
                open('movielist.txt','a').write(date+'   ')

            pretag = re.compile(r'genre')
            afttag = re.compile(r'</span>')
            pretaglist = re.findall(pretag,content)
            afttaglist = re.findall(afttag,content)
            pretaglocate = 0
            tags = ['']*10
            p = 0
            while pretaglocate != -1:
                pretaglocate = pretaglocate + 5
                pretaglocate = content.find(pretaglist[0],pretaglocate)
                afttaglocate = content.find(afttaglist[0],pretaglocate)
                if pretaglocate !=-1:
                    tags[p] = content[pretaglocate+7:afttaglocate]
                    print tags[p]
                    open('movielist.txt','a').write(tags[p]+'   ')
                p+=1
            else:
                open('movielist.txt','a').write('\n')
                print "tags over"
            print "url over"
    else:
        print flag
print "This user text has finished!"
