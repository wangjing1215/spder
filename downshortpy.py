#-*- coding=UTF-8 -*-
import requests as a
import os
import re
import time
def loppget(url):
    user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    headers={'User-Agent':user_agent}
    #resmv=a.get(url='http://ww.baidu.com')
    try:
        resmv=a.get(url=url,headers=headers)
    except:
        resmv=loppget(url)
    return  resmv

    
user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
headers={'User-Agent':user_agent}
url1='网站地址'
res=loppget(url1)
print 3
p=r'href="(http://miaopaiku.+?.html)"'#匹配规则
pp=re.compile(p)
list1=pp.findall(res.content)
new_li=[]
for num in list1:
    if num not in new_li:
        new_li.append(num)
print new_li
for i in new_li:
    time.sleep(0)
    urlmv=i
    resmv=loppget(urlmv)
        
    #print resmv.text
    pmv=r'url="(.+?.mp4)"'
    ppmv=re.compile(pmv)
    listmv=ppmv.findall(resmv.content)
    if listmv==[]:
        continue
    pnm=r"<title>(.+?)</title>"
    ppnm=re.compile(pnm)
    listnm=ppnm.findall(resmv.content)
    filenm=listnm[0]
    filename=filenm.decode('utf-8').encode('gbk')
    filename=filename[0:filename.find('|')]
    filepath='E:\\sp\\shourtmv\\'+filename+'.mp4'
    if os.path.exists(filepath):
        print 'this '+filename+' have exists'
        continue
    print filename+'start to get'
    try:
        time.sleep(1)
        rests=a.get(url=listmv[0],headers=headers)
        print '*======get the date'
    except:
        print 'worng requests!'
        continue
    with open(filepath, 'ab+') as f:
        f.write(rests.content)
        f.flush()
    print filename+' has done!'

