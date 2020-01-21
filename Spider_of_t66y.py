import requests
import threading
from bs4 import BeautifulSoup
from lxml import html
import xml
import sys
import argparse 
import os
import time

class_list1=["[亞洲]","[歐美]","[動漫]","[寫真]","[原创]","[其它]"]
main_url="http://t66y.com/"
url1="http://t66y.com/thread0806.php?fid=8&search=&page="
url2="http://t66y.com/thread0806.php?fid=16&search=&page="
max_thread=200

def download_pic(name,url,path): #该函数用于下载具体帖子内的图片
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
    photo_num=len(photo_list)
    for li in photo_list:
        #print(str(li))
        pic_url=str(li).split('"')[-2]
        print("download:",pic_url,end="")
        try:
            r=requests.get(pic_url,stream=True)
        except:
            print("connect failed...")
            return 0
        if r.status_code==200:
            count+=1
            open(savepath+"/"+str(count)+"."+pic_url.split(".")[-1], 'wb').write(r.content)
            print("(",count+1,"/",photo_num,")")
        else:
            print("request failed!")
        del r

def get_list(class_name,url): #该函数获取板块内的帖子列表
    '''get_list(class_name,url)'''
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
        while(1):
            if threading.active_count()<max_thread:
                break
            else:
                time.sleep(1)
        download_thread=threading.Thread(target=download_pic, args=(key,post_list[key],"./t66y/"+class_name,)) #多线程下载
        download_thread.setDaemon(True)  #设置守护进程
        download_thread.start()
        time.sleep(0.1)

def pre_exit():
    while(1):
        thread_unfinished=threading.active_count() - 1
        if thread_unfinished>0:
            print("\n***剩余下载线程：[",thread_unfinished,"]***")
            print("若长时间响应请手动结束进程...")
            time.sleep(8)
        else:
            print("下载已完成！")
            exit(0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--class_id',type=int,default=0,help="'1' for 【新時代的我們】, '2' for 【達蓋爾的旗幟】, '0' for both")
    parser.add_argument('-s','--start',type=int,default=1,help="Page_start(default=1)")
    parser.add_argument('-e','--end',type=int,default=1,help="Page_end")
    parser.add_argument('-m','--max_thread',type=int,default=200,help="Max thread num(default=200)")
    args = parser.parse_args()
    class_id=args.class_id
    start=args.start
    end=args.end
    if class_id>2:
        print("Sorry no class [",class_id,"] !")
        exit(0)
    if end<start or start<1:
        print("Bad range!")
        exit(0)
    if os.path.exists("./t66y"):
        print("path[',/t66y'] exists")
    else:
        os.mkdir("./t66y")
    print("Enjoy your life!")
    if class_id==0:
        print("将下载【新時代的我們】和【達蓋爾的旗幟】的图片...")
        for i in range(start,end+1):
            print("开始下载第",i,"页")
            get_list("新時代的我們",url1+str(i))
            get_list("達蓋爾的旗幟",url2+str(i))
        pre_exit()
    else:
        if class_id==1:
            print("将下载【新時代的我們】的图片...")
            for i in range(start,end+1):
                print("开始下载第",i,"页")
                get_list("新時代的我們",url1+str(i))
            pre_exit()
        if class_id==2:
            print("将下载【達蓋爾的旗幟】的图片...")
            for i in range(start,end+1):
                print("开始下载第",i,"页")
                get_list("達蓋爾的旗幟",url2+str(i))
            pre_exit() 

if __name__=="__main__":
    main()
