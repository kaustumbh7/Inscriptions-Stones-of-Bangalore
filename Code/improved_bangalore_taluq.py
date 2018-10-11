# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 12:44:46 2018

@author: Dhairya and Kaustumbh
"""
# Reading the file 
text_file = open("Bangalore_Taluq.txt", "r",encoding="utf8")
str1 = text_file.read()

# Removing all diacritical marks
str1 = str1.replace("-"," ")
str1 = str1.replace("."," ")
str1 = str1.replace("("," ")
str1 = str1.replace(")"," ")
str1 = str1.replace(","," ")
str1 = str1.replace("^"," ")
str1 = str1.replace("\n"," ")
str1 = str1.replace(";"," ")
str1 = str1.replace("}"," ")
str1 = str1.replace("{"," ")
str1 = str1.replace("—"," ")
str1 = str1.replace(":"," ")
str1 = str1.replace("·"," ")
str1 = str1.replace("'ll"," will")
str1 = str1.replace("'nt"," not")
str1 = str1.replace("?"," ")
str1 = str1.replace("!"," ")
str1 = str1.replace(">"," ")
str1 = str1.replace("<"," ")
str1 = str1.replace("&"," ")
str1 = str1.replace("/"," ")
str1 = str1.replace("|"," ")
str1 = str1.replace("~"," ")
str1 = str1.replace("@"," ")
str1 = str1.replace("["," ")
str1 = str1.replace("]"," ")
str1 = str1.replace("δ"," ")
str1 = str1.replace("ό"," ")
str1 = str1.replace("="," ")

str1 = str1.replace("à","a")
str1 = str1.replace("á","a")
str1 = str1.replace("â","a")
str1 = str1.replace("ä","a")
str1 = str1.replace("æ","a")
str1 = str1.replace("ã","a")
str1 = str1.replace("å","a")
str1 = str1.replace("ā","a")
str1 = str1.replace("a","a")

str1 = str1.replace("è","e")
str1 = str1.replace("é","e")
str1 = str1.replace("ê","e")
str1 = str1.replace("ë","e")
str1 = str1.replace("ē","e")
str1 = str1.replace("ė","e")
str1 = str1.replace("ę","e")

str1 = str1.replace("ÿ","y")

str1 = str1.replace("û","u")
str1 = str1.replace("ü","u")
str1 = str1.replace("ù","u")
str1 = str1.replace("ú","u")
str1 = str1.replace("ū","u")

str1 = str1.replace("î","i")
str1 = str1.replace("ï","i")
str1 = str1.replace("í","i")
str1 = str1.replace("ī","i")
str1 = str1.replace("į","i")
str1 = str1.replace("ì","i")

str1 = str1.replace("ñ","n")
str1 = str1.replace("ń","n")

str1 = str1.replace("ô","o")
str1 = str1.replace("ö","o")
str1 = str1.replace("ò","o")
str1 = str1.replace("ó","o")
str1 = str1.replace("œ","o")
str1 = str1.replace("ø","o")
str1 = str1.replace("ō","o")
str1 = str1.replace("õ","o")

str1 = str1.replace("ś","s")
str1 = str1.replace("š","s")

str1 = str1.replace("ł","l")

str1 = str1.replace("ž","z")
str1 = str1.replace("ź","z")
str1 = str1.replace("ż","z")

str1 = str1.replace("ç","c")
str1 = str1.replace("ć","c")
str1 = str1.replace("č","c")

str1 = str1.lower()

# Creating copy of str1 (to be used later)
str2 = str1 

l1 = str1.split("****")

for i in range(len(l1)):
    l1[i] = l1[i].split(' ')
    
text_file_2 = open("English_Words.txt", "r")
lines = text_file_2.read().split("\n")

# Removing English words
for j in range(len(l1)):
    for i in l1[j]:
        if i in lines:
            l1[j].remove(i)
        if i == "":
            l1[j].remove(i)
        if i.isdigit():
            l1[j].remove(i)

# Correcting the errors            
import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction_propernoun(word): 
    "Most probable spelling correction for word."
    return max(candidates_propernoun(word), key=P)

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates_propernoun(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or [word])

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Avoiding correction of proper nouns
propernouns = []

for i in range(len(l1)):
    for j in range(len(l1[i])):
        result = correction_propernoun(l1[i][j])
        if (result == l1[i][j]):
            propernouns.append(result)
            
propernouns_str = ' '.join(str(v) for v in propernouns)

# Writimg the list of proper nouns generated to a file 
with open('proper_nouns_final_1.txt', 'a',encoding="utf8") as the_file:
    the_file.write(propernouns_str)
            
text_file_3 = open("proper_nouns_final_1.txt", "r",encoding="utf8")
lines2 = text_file_3.read().split(" ")

errors = []

for i in l1:
    for j in i:
        errors.append(j)
 
# Removing the proper nouns        
for i in errors:
    if i in propernouns:
        errors.remove(i)
    
correct = []

# Correcting the English word errors 
for i in errors:
    result = correction(i)
    correct.append(result)
    

# Removing diacritical marks froms str2
str2 = str2.lower()
str2 = str2.replace("("," ")
str2 = str2.replace("\n"," ")
str2 = str2.replace(")"," ")
str2 = str2.replace("["," ")
str2 = str2.replace("]"," ")
str2 = str2.replace("δ"," ")
str2 = str2.replace("ό"," ")
str2 = str2.replace("="," ")
str2 = str2.replace("à","a")
str2 = str2.replace("á","a")
str2 = str2.replace("â","a")
str2 = str2.replace("ä","a")
str2 = str2.replace("æ","a")
str2 = str2.replace("ã","a")
str2 = str2.replace("å","a")
str2 = str2.replace("ā","a")
str2 = str2.replace("a","a")
str2 = str2.replace(",",";")


str2 = str2.replace("è","e")
str2 = str2.replace("é","e")
str2 = str2.replace("ê","e")
str2 = str2.replace("ë","e")
str2 = str2.replace("ē","e")
str2 = str2.replace("ė","e")
str2 = str2.replace("ę","e")

str2 = str2.replace("ÿ","y")
str2 = str2.replace("û","u")
str2 = str2.replace("ü","u")
str2 = str2.replace("ù","u")
str2 = str2.replace("ú","u")
str2 = str2.replace("ū","u")

str2 = str2.replace("î","i")
str2 = str2.replace("ï","i")
str2 = str2.replace("í","i")
str2 = str2.replace("ī","i")
str2 = str2.replace("į","i")
str2 = str2.replace("ì","i")

str2 = str2.replace("ñ","n")
str2 = str2.replace("ń","n")

str2 = str2.replace("ô","o")
str2 = str2.replace("ö","o")
str2 = str2.replace("ò","o")
str2 = str2.replace("ó","o")
str2 = str2.replace("œ","o")
str2 = str2.replace("ø","o")
str2 = str2.replace("ō","o")
str2 = str2.replace("õ","o")

str2 = str2.replace("ś","s")
str2 = str2.replace("š","s")

str2 = str2.replace("ł","l")

str2 = str2.replace("ž","z")
str2 = str2.replace("ź","z")
str2 = str2.replace("ż","z")

str2 = str2.replace("ç","c")
str2 = str2.replace("ć","c")
str2 = str2.replace("č","c")


# Replacing error words in the text to generate corrected text
lst_index=[]
for i in range(len(errors)):
    if errors[i] in lines_kan:
        lst_index.append(errors[i])
        
lst_str2 = str2.split(" ")

for i in range(len(errors)):
    for j in range(len(lst_str2)):
        if errors[i]==lst_str2[j]:
            lst_str2[j]=correct[i]
            
str3 = " ".join(str(v) for v in lst_str2)
str3 = str3.replace("****",",")

with open('bangalore_taluq_automated_corrections_1.csv', 'a',encoding="utf8") as the_file:
    the_file.write(str3)

# Storing the corrected text as per the inscription number in a CSV file     
import csv
from itertools import izip
a = zip(*csv.reader(open("bangalore_taluq_automated_corrections_1.csv","rt",encoding="utf8")))
csv.writer(open("output.csv", "wt",encoding="utf8")).writerows(a)



    