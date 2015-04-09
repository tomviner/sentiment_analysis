# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:50:56 2015

@author: lili.tcheang
"""
from textblob import TextBlob
import glob
#print glob.glob("*.txt")

articles = []
for filename in glob.glob("*.txt"):
    file_content = open(filename).read()
    articles.append(unicode(file_content,"utf-8"))
    
#print articles

def score(text):
    tb = TextBlob(text)
    return tb.sentiment.polarity
    
    
    
def sort_articles(art):
    
    return sorted(art,key=score)    
#==============================================================================
# wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# wiki = TextBlob("Lili is very happy and awesome and annoying!")
# 
# print wiki.tags
#==============================================================================

print sort_articles(articles)