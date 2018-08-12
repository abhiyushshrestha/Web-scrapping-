#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:01:42 2018

@author: abhiyush
"""

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

#Just practicing to scrape the data using beautifulsoup

#******************************************************************************
url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

page = requests.get(url)

page.status_code

page.text

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

soup.find_all('p')
soup.find_all('br')
soup.find_all('h1')

soup.find_all('p')[2]
soup.find_all('p')[2].get_text()

soup.find_all(class_ =  'chorus')

soup.find_all('p', class_ = 'chorus')

soup.find_all(id = 'fourth')

#******************************************************************************

# Colecting the name of artist of only one page

#******************************************************************************
# Collect and parse first page 
url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all the text from the BodyText div
artist_name_list = soup.find(class_ = "BodyText")

# Pull text from all the instances of <a> tag within the bodytext div
artist_name_list_items = artist_name_list.find_all('a')

#Remove bottom link
last_links = soup.find(class_ = 'AlphaNav')
last_links_decompose = last_links.decompose()

for artist_name in artist_name_list_items:
    print(artist_name.prettify())
    
# Create a file to write to, add headers row
f = csv.writer(open('/home/abhiyush/mPercept/Web crawling/web_crawling_artist_name.csv', 'w'))
f.writerow(['Name', 'Link'])

names = []
links = []    
for artist_name in artist_name_list_items:
    names.append(artist_name.contents[0])
    links.append('https://web.archive.org' + artist_name.get('href'))

    
artist_name_df = pd.DataFrame(names,  columns = ['Artist names'])
artist_name_df['Links'] = pd.DataFrame(links)

artist_name_df.to_csv("artist_name.csv")

#******************************************************************************

# To scrape name of all the artist by traversing through all the available pages

#******************************************************************************
urls = []
names = []
links = [] 
for i in range(1,5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) +'.htm'
    urls.append(url)
    
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    last_links = soup.find(class_ = "AlphaNav")
    last_links.decompose()
    
    artist_name_list = soup.find(class_ = "BodyText")
    artist_name_list_items = artist_name_list.find_all('a')
    
     
    for artist_name in artist_name_list_items:
        names.append(artist_name.contents[0])
        links.append('https://web.archive.org' + artist_name.get('href'))

artist_name_df = pd.DataFrame(names,  columns = ['Artist names'])
artist_name_df['Links'] = pd.DataFrame(links)
artist_name_df.to_csv("artist_name.csv")

#******************************************************************************


