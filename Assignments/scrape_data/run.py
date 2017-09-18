# -*- coding: utf-8 -*-
# Program: Scraping Data
# Name: Muni Bhupathi Reddy Dandu
# Mwsu-Id: M20228454

import requests
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

outfile=open("products.csv","w")
category="item_name,shipping_info\n"
outfile.write(category)
count=0
item_list=[]
for page in range(1,4):
    my_url="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=mobile&bop=And&Page="+str(page)+"&PageSize=36&order=BESTMATCH"
    page_html=urlopen(my_url).read()
    soup=BeautifulSoup(page_html,"html.parser")
    item_containers=soup.findAll("div",{"class":"item-container"})	#finds the class names with the given html element
    # print(len(containers))
    # print(containers[0])
    # container=containers[0]
    for container in item_containers:
        title_container=container.findAll("a",{"class":"item-title"})	#finds all the class names(item-title) with given html element(a)
        item_name=title_container[0].text	#stores text of first element in container
        shipping_container=container.findAll("li",{"class":"price-ship"})
        shipping_info=shipping_container[0].text.strip() #strip removes all the unnecessary spaces
        # print(title_container)
        # print("product: ",item_name)
        # print("shipping: ",shipping_info)
        if count==100:
            break
        count=count+1
        outfile.write(item_name.replace(","," ")+","+shipping_info+"\n")
outfile.close()
