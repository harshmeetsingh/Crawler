from tkinter import *
from bs4 import BeautifulSoup 
import re
import requests
import os
import sys

http_proxy  = "http://ayush.goyal:lmalftanso@202.141.80.24:3128"
https_proxy = "https://ayush.goyal:lmalftanso@202.141.80.24:3128"
ftp_proxy   = "ftp://ayush.goyal:lmalftanso@202.141.80.24:3128"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }
def Close_func():
    gui.destroy()

def Re():
    gui.destroy()
    CallBack()
def Info_channel():

    
    links=link.get()
    r=requests.get(links,proxies=proxyDict)
    soup=BeautifulSoup(r.content,"lxml")
    channelname= "Channel Name:" + soup.title.string
    first=Label(text=channelname,fg='orange',bg='black').place(x=0,y=0)
    vid_name,viewstr,view_count,disp_link=None,None,None,None
    
    placer=0
    placer1 = 0
    space = 0
    
    for anchor in soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"):
        vid_name=anchor.text
        second=Label(text=vid_name,fg='black',bg='white').place(x=200,y=40+space)
        space=space+20
    desc_list=soup.find_all(attrs={'name':'description'})
    desc=desc_list[0]['content']#.encode('utf-8')
    third=Label(text=desc,fg='black',bg='red').place(x=0,y=20)
    view_tags = soup.find_all('li', text=re.compile("[\d,]+ views"))
    for view_tag in view_tags:
        views = re.findall(r'[\d,]+', view_tag.text)[0]
        view_count=Label(text=views,fg='blue').place(x=650,y=40+placer)
        placer=placer + 20
            
    for all_links in soup.find_all('a', class_="yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2"):
        vid_link=all_links.get('href')
        final_link="https://www.youtube.com"+vid_link
        disp_link=Label(text=final_link).place(x=750,y=40+placer1)
        placer1=placer1+20
        
        
gui=Tk()
gui.geometry('500x400')
gui.title('YouTube Crawler')
label=Label(text='Paste Link Here',fg='blue')
label.pack()
link=StringVar()
entry=Entry(gui,textvariable=link)
entry.pack()
channel=Button(text='Crawl this Channel',fg='white',bg='black',width=30,command=Info_channel)
Restart=Button(text='Crawl another Channel',fg='white',bg='black',width=20,command=Re)
Stop=Button(text='Close',fg='white',bg='black',width=15,command=Close_func)



channel.place(x=10,y=45)
Restart.place(x=10,y=75)
Stop.place(x=10,y=105)

entry.focus_set()
url=entry.get()

def CallBack():
    os.system('YouTube_Crawler.py')
gui.mainloop()


        
        
    
    