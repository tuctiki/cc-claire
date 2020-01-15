import requests
import threading
from bs4 import BeautifulSoup
from lxml import html
import xml
import os
import time

class_list1=["[亞洲]","[歐美]","[動漫]","[寫真]","[原创]"]

main_url="http://t66y.com/"
url1="http://t66y.com/thread0806.php?fid=8&search=&page="
url2="http://t66y.com/thread0806.php?fid=16&search=&page="

if os.path.exists("./t66y"):
    print("path[',/t66y'] exists")
else:
    os.mkdir("./t66y")

def download_pic(name,url,path):
    count=-1
    try:
        os.mkdir(path+"/"+name[:4])
    except:
        pass
    if os.path.exists(path+"/"+name[:4]+"/"+name[4:]):
        print("path['"+path+"/"+name[:4]+"/"+name[4:]+"'] exists")
        return 0
    else:
        os.mkdir(path+"/"+name[:4]+"/"+name[4:])
    try:
        f=requests.get(url)
    except:
        print("download failed...")
        return 0
    soup=BeautifulSoup(f.content,"lxml")
    photo_div=soup.find_all('div',class_="tpc_content do_not_catch")
    photo_list=photo_div[0].find_all('img')
    savepath=path+"/"+name[:4]+"/"+name[4:]
    for li in photo_list:
        print(str(li))
        pic_url=str(li).split('"')[-2]
        print(pic_url)
        try:
            r=requests.get(pic_url,stream=True)
        except:
            print("connect failed...")
            return 0
        if r.status_code==200:
            count+=1
            open(savepath+"/"+str(count)+"."+pic_url.split(".")[-1], 'wb').write(r.content)
        else:
            print("request failed!")
        del r

def get_list(class_name,url):
    if os.path.exists("./t66y/"+class_name):
        print("path['./t66y/"+class_name+"'] exists")
    else:
        os.mkdir("./t66y/"+class_name)
    post_class=""
    try:
        f=requests.get(url)
    except:
        print("Connect failed!")
        exit()
    soup=BeautifulSoup(f.content,"lxml")
    td=soup.find_all('td',class_="tal")
    post_list=dict()
    for i in td:
        if "↑" in str(i):  #过滤几个置顶公告帖
            continue
        for item in class_list1:
            if item in str(i):
                post_class=item
                break
            else:
                post_class="[其它]"
        post_title=i.find_all('h3')[0].find_all('a')[0].string
        post_title=post_class+post_title
        post_url=str(i.find_all('h3')[0]).split('"')[1]
        post_url=main_url+post_url
        post_list[post_title] =post_url
    print(post_list)
    for key in post_list:
        #download_pic(key,post_list[key],"./t66y/"+class_name)
        download_thread=threading.Thread(target=download_pic, args=(key,post_list[key],"./t66y/"+class_name,))
        download_thread.start()
        time.sleep(0.5)

print("适当看图怡情，过度手冲伤身！")
page_to_down=int(input("输入你要下载的页数（大于1）："))
if page_to_down<1:
    exit()
else:
    if page_to_down==1:
        page_to_down+=1
for i in range(1,page_to_down):
    get_list("新時代的我們",url1+str(i))
    get_list("達蓋爾的旗幟",url2+str(i))
