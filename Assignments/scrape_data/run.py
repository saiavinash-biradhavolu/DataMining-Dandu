# -*- coding: utf-8 -*-
# Program: Scraping Data
# Name: Muni Bhupathi Reddy Dandu
# Mwsu-Id: M20228454

import requests
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

my_url="https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=mobile&bop=And&PageSize=96&order=BESTMATCH"
page_html=urlopen(my_url).read()
soup=BeautifulSoup(page_html,"html.parser")
item_containers=soup.findAll("div",{"class":"item-container"})	#finds the class names with the given html element
# print(len(containers))
# print(containers[0])
# container=containers[0]
outfile=open("products.csv","w")
category="item_name,shipping_info\n"
outfile.write(category)
for container in item_containers:
	title_container=container.findAll("a",{"class":"item-title"})	#finds all the class names(item-title) with given html element(a)
	item_name=title_container[0].text
	shipping_container=container.findAll("li",{"class":"price-ship"})
	shipping_info=shipping_container[0].text.strip() #strip removes all the unnecessary spaces
	# print(title_container)
	# print("product: ",item_name)
	# print("shipping: ",shipping_info)
	outfile.write(item_name+","+shipping_info+"\n")
outfile.close()
