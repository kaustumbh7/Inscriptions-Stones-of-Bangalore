#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:29:33 2018

@author: Kaustumbh and Dhairya
"""

text_file2 = open("Proper_nouns.txt", "r")
lines2 = text_file2.read().split("\n")


l1_copy = l1.copy()

for i in l1_copy:
    for j in i:
        if j in lines2:
            i.remove(j)


str1_copy = str1

for i in range(len(str1_copy)-1):
    if str1_copy[i] == " " and str1_copy[i+1] == " ":
        str1_copy.replace(str1_copy[i],"")
        

str1_copy = str1_copy.replace("                        ","")


l1_copy_2 = []
for i in l1_copy:
    for j in i:
        l1_copy_2.append(j)
            
l1_copy_2_str = " ".join(str(v) for v in l1_copy_2)




str1_lst = str1_copy.split(" ")

for i in str1_lst:
    if i == "":
        str1_lst.remove(i)



lst_of_lst = [[]  for v in range(len(l1_copy_2))]
k = 0 
for i in l1_copy_2:
    for j in range(2,len(str1_lst)-2):
        if i == str1_lst[j] and i != " ":
            print(i,j)
            print(str1_lst[j-1])
            lst_of_lst[k].append(str1_lst[j-2])
            lst_of_lst[k].append(str1_lst[j-1])
            lst_of_lst[k].append(str1_lst[j])
            lst_of_lst[k].append(str1_lst[j+1])
            lst_of_lst[k].append(str1_lst[j+2])
            k = k + 1


lst_of_lst_2 = [] # Has the desired query format
for i in lst_of_lst:
    lst_of_lst_str = "+".join(str(v) for v in i)
    lst_of_lst_2.append(lst_of_lst_str)

###############################################################################
            

from lxml.html import fromstring
from requests import get


lst_str2 = []

for i in lst_of_lst_2:
    query = i 
    str2 = get("http://www.google.com/search?q=" + query).text
    lst_str2.append(str2)
    #print(str2)

lnt = len(str2)


ans_lst = []
dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']


for i in lst_str2:
    str2 = i


    str2 = str2.replace("-"," ")
    str2 = str2.replace("."," ")
    str2 = str2.replace("("," ")
    str2 = str2.replace(")"," ")
    str2 = str2.replace(","," ")
    str2 = str2.replace("^"," ")
    str2 = str2.replace("\n"," ")
    str2 = str2.replace(";"," ")
    str2 = str2.replace("}"," ")
    str2 = str2.replace("{"," ")
    str2 = str2.replace("—"," ")
    str2 = str2.replace(":"," ")
    str2 = str2.replace("·"," ")
    str2 = str2.replace("'ll"," will")
    str2 = str2.replace("'nt"," not")
    str2 = str2.replace("?"," ")
    str2 = str2.replace("!"," ")
    str2 = str2.replace(">"," ")
    str2 = str2.replace("<"," ")
    str2 = str2.replace("&"," ")
    str2 = str2.replace("/"," ")
    str2 = str2.replace("|"," ")
    str2 = str2.replace("~"," ")
    str2 = str2.replace("@"," ")
    str2 = str2.replace("["," ")
    str2 = str2.replace("]"," ")
    str2 = str2.replace("_","")
    
        
    
    lst = str2.split(" ")
    
    loc = 0
    
    for i in range(len(lst)):
        if lst[i] == 'Showing':
            loc = i 
            break
        if lst[i] == 'mean':
            loc = i
            break
    
    if loc!=0:
        lst2 = lst[loc:loc+20]
    
    for i in lst2:
        for j in range(len(i)-2):
            if i[j] == 'q' and i[j+1] == '='and i[j+2] in dic:
                ans = i
    
    ans = ans[2:]
    
    ans = ans.replace('+'," ")
    
    ans_lst.append(ans)
