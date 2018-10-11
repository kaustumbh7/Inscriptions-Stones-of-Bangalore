#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 23:47:55 2018

@author: Kaustumbh and Dhairya
"""

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

lst = []

# Value in range specifies the no. of pages in the particular volume
for i in range(323):
    if i >= 1:
        num = '000' + str(i)
    if i >= 10:
        num = '00' + str(i)
    if i >= 100:
        num = '0' + str(i)
    if i >= 1000:
        num = str(i)

    # specify the url
    quote_page = "http://idb.ub.uni-tuebingen.de/diglit/EC_17_1965/" + num

    # query the website and return the html to the variable ‘page’
    page = urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('div', attrs={"id": "tab_text_ocr"})

    name = name_box.text.strip() # strip() is used to remove starting and trailing
    
    lst.append(name)
    print(i)    


lst2 = lst.copy()

# Extracting the required text by removing the extra spaces
for i in range(len(lst2)):
    #lst2[i] = 'Page_break\n' + lst2[i][110:-261]
    lst2[i] = 'Page_break\n' + lst2[i][87:-87] 



str_2 = " ".join(str(v) for v in lst2)

# Storing the text in a file 
with open("Volume_17.txt", 'a', encoding='utf8') as the_file:
    the_file.write(str_2)
    
    


