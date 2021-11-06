#!/usr/bin/env python3
"""mapper.py"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import requests
session = requests.Session()
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    try:
        count = int(words[1])
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        print("error, incorrect input")
        exit()
    count = int(words[1])
    cur_urls = []
    new_list = [words[0]]
    links = set()
    mapping = {}
    for i in range(0,count):
        # print("run",i)
        cur_urls= new_list
        new_list = []
        for url in cur_urls:
            # print(url)
            req = ""
            html_page = ""
            try:
                req = Request(url)
                html_page = urlopen(req)
            except:
                continue
            if(html_page.getcode()!=200):
                continue
            # print(html_page.getcode())
            mapping[url] = []
            soup = BeautifulSoup(html_page, "lxml")

            for link in soup.findAll('a'):
                new_link = link.get('href')
                if new_link not in links and new_link is not None and new_link.startswith('http'):
                    try:
                        # print(new_link)
                        session.get(url)
                        links.add(new_link)
                        new_list.append(new_link)
                        mapping[url].append(new_link)
                    except:
                        continue
    
    print("links","\t",len(links))
    edges = 0
    for i in mapping:
        edges+=len(mapping[i])
    print("edges","\t",edges)

    for i in mapping:
        for j in mapping[i]:
            print(i,"\t",j)
