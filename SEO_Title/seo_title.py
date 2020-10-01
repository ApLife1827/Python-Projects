# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 07:16:01 2019

@author: avdhoot
"""

from urllib.request import urlopen,Request 
import bs4 as bse
import re

url=input("Which page would you like to check? Enter Full URL:")
keyword=input("What is your seo keyword? ")
keyword=keyword.casefold()
try:
    req=Request(url,headers={'User-Agent':'Mozilla/6.0'})
    html=urlopen(req)
except HTTPError as e:
    print(e)
data=bse.BeautifulSoup(html,"html.parser")
 
def seo_title_found(keyword,data):
    if data.title:
        if keyword in data.title.text.casefold():
            status="Keyword Found"
        else:
            status="Keyword Not found"
    else:
        status="Not title found"
    return status

def seo_title_stop_words(data):
    words=0
    list_words=[]
    if data.title:
        with open('Stop_word.txt','r') as f:
            for line in f:
                if re.search(r'\b'+line.rstrip('\n') + r'\b',data.title.text.casefold()):
                    words+=1
                    list_words.append(line.rstrip('\n'))
        if words>0:
            stop_words="We found {} stop words in your title. You should consider removing them".format(words,list_words)
        else:
            stop_words="We found no stop words in the title. Good work!"
    else:
        stop_words="We could not find a title"
    return stop_words

def seo_title_length(data):
    if data.title:
        if len(data.title.text)<60:
            length="Your length is under the maximum suggested length of 60characters. Your title is {}".format(len(data.title.text))
        else:
            length="Your length is over the maximum suggested length of 60characters. Your title is {}".format(len(data.title.text))
    else:
        length="No title was found"
    return length

def seo_url(url):
    if url:
        if keyword in url:
            slug="Your keyword was found in your slug"
        else:
            slug="Your keyword was not found in your slug. It is suggested to add your keyword to your slug."
    else:
        slug="No url was returned."

    return slug

def seo_url_length(url):
    if url:
        if len(url)<100:
            url_length="Your url is less than the 100 character maximum suggested length. Good work"
        else:
            url_length="Your url is over 100 character. Your url currently is {}. You should change this.".format(len(url))
    else:
        url_length="URL was not found"

    return url_length

def seo_h1(keyword,data):
    total_h1=0
    total_keyword_h1=0
    if data.h1:
        all_tags=data.find_all('h1')
        for tag in all_tags:
            total_h1+=1
            tag=str(tag.string)
            if keyword in tag.casefold():
                total_keyword_h1+=1
                h1_tag="Found keyword in h1 tag. You have total of {} H1 tags and your keyword found in {} of them".format(total_h1,total_keyword_h1)
            else:
                h1_tag="Did not find a keyword in h1 tag."

    else:
        h1_tag="No H1 tags found"

    return h1_tag

print(seo_title_found(keyword,data))
print(seo_title_stop_words(data))
print(seo_title_length(data))
print(seo_url(url))
print(seo_url_length(url))
print(seo_h1(keyword,data))
