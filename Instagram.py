# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:58:02 2019

@author: Faiz
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
#import ssl
import requests
#import random
#import os

def getinfo(soup):
    data=soup.find_all('meta',{'property':'og:description'})
    #print(data[0])
    text=data[0].get('content').split()
    #print(text)
    user="%s %s %s"%(text[-3],text[-2],text[-1])
    followers=text[0]
    following=text[2]
    posts=text[4]
    print("User:",user)
    print("Followers:",followers)
    print("Following:",following)
    print("Posts:",posts)
    a="User: "+user
    b="Followers: "+followers
    c="Following: "+following
    d="Posts: "+posts
    s=a+"\n"+b+"\n"+c+"\n"+d
    filename=insta_username+".txt"
    with open(filename,"w+") as f1:
        f1.write(s)
        
def getstatus(soup):
    contempt=soup.find('script',{'type':'application/ld+json'})
    #print(contempt.text)
    if contempt==None:
        return 0
    a=contempt.text.find("description")
    b=contempt.text.find("mainEntityofPage")
    sentence=contempt.text[a+14:b-3]
    l=sentence.split("\\n")
    #print(l)
    status=""
    for i in l:
        status=status+"\n"+i
    print(status)
    filename=insta_username+".txt"
    with open(filename,"a") as f2:
        f2.write(status)
    
def getimage(soup):
    contempt=soup.find('script',text=lambda t: t.startswith('window._sharedData'))
    #print(contempt1)
    test_string=contempt.text
    a=test_string.find("profile_pic_url_hd")+21
    b=test_string.find("requested_by_viewer")-3
    string_url=test_string[a:b]
    #print(string_url)
    print("\n \n downloading")
    filename=insta_username+".jpg"
    with open(filename,"wb+") as f:
        response=requests.get(string_url,stream=True)
        if not response.ok:
            print(response)
        for i in response.iter_content(1024):
            if not i:
                break
            f.write(i)
    print("\n       downloading complete.........")
                
        

#ctx=ssl.create_default_context()
#ctx.check_hostname=False
#ctx.verify_mode=ssl.CERT_NONE
insta_url="https://www.instagram.com/"
insta_username=input("Enter the user name: ")
insta_address=insta_url+insta_username+"/"
#print(insta_address)
try:
    page = urlopen(insta_address)
except:
    print("Could not load page")
soup = BS(page, 'html.parser')

getinfo(soup)
getstatus(soup)
getimage(soup)
