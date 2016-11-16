# -*- coding: UTF-8 -*-
import MySQLdb as mdb
import sys
import content
import xietong
import svd_result


def Update(n):
  if(n==0):
    print "xietong"
    print "svd"
    xietong.xietong_update();
    svd_result.svd_update();
  if(n==1):
    print "xietong"
    xietong.xietong_update();
  if(n==2):
    print "svd"
    svd_result.svd_update();
  if(n==3):
    print "svd"
    content.content_update();
  if(n==4):
    print "xietong"
    print "svd"
    print "content"
    xietong.xietong_update();
    svd_result.svd_update();
    content.content_update();
    
    
