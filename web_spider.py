#imports    
import os
import sys
import io
import urllib
import urllib.request as ur
from bs4 import BeautifulSoup


##clears

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

## intro_banner


def intro ():
    print("""
               _                 _     _           
 __      _____| |__    ___ _ __ (_) __| | ___ _ __ 
 \ \ /\ / / _ \ '_ \  / __| '_ \| |/ _` |/ _ \ '__|
  \ V  V /  __/ |_) | \__ \ |_) | | (_| |  __/ |   
   \_/\_/ \___|_.__/  |___/ .__/|_|\__,_|\___|_|   
                          |_|                      

           [+] Coded By : Aidin Mansouri [+]
                Welcome To Webspider !

    """)
## help
def helpy():
    print("""
    1. To get link 
    2. To get pictures 
    3. To get source
    4. Help 
    5. Clear
    6. Exit
    """)
## functions
def get_link():
    req=input("Do you want to save in a file ? (y/n) ")
    if req == 'y':
        for s in scrapy.find_all('a'):
            scrapy1=s.get('href')
            with io.open("links.txt", "w", encoding="utf-8") as f:
                f.write(str(scrapy1)+"\n")
        f.close()
        print("links.txt created successfully")
    else:
        for s in scrapy.find_all('a'):
            scrapy1=s.get('href')
            print(scrapy1+"\n")

def get_pic():
    req=input("Do you want to save in a file ? (y/n) ")
    if req == 'y':
        for img in scrapy.find_all('img'):
            scrap=img.get('src=')
            with io.open("links.txt", "w", encoding="utf-8") as f:
                f.write(str(scrap)+"\n")
        f.close()
        print("pic.txt created successfully")
    else:
        for img in scrapy.find_all('img'):
            scrap=img.get('src=')
            scrap=str(scrap)
            print(scrap+"\n")

def get_source():
    fl=open('source.html','w+')
    for c in str(source):
        fl.write(c)
    fl.close()
    print("Successful")
#--------------------------------------


##core 
while True:
    try:
        url=input("please enter your site (with no http:// ) : ")
        link = ur.urlopen("http://"+url)
        break
    except urllib.error.URLError:
        print("please enter a valid url ")
    except UnicodeEncodeError:
        print("please enter a valid url ")

        
source=link.read()
scrapy = BeautifulSoup(source,'html.parser')

##loop 
clear()
intro()

while True:
    helpy()
    a=input("~>> ")
    if a == '1':
        get_link()
    elif a == '2':
        get_pic()
    elif a == '3':
        get_source()
    elif a == '4':
        helpy()
    elif a == '5':
        clear()
    elif a== '6' :
        break
    else:
        print("type '4'  for help ")
    