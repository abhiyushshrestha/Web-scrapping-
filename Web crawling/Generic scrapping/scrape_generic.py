#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:15:47 2018

@author: abhiyush
"""

import requests
from bs4 import BeautifulSoup

class scrape:
    url = ""
    
    def __init__(self, url):
        self.url = url
        
    def scrapping(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        return soup
    
    def get_links(self, soup):
        return soup.find_all('a')
    
    def separate_links(self, links):
        urls = []
        for link in links:
            link = link['href']
            link = link.strip()
            if len(link) < 10:
                continue
            urls.append(link)
        
        urls = set(urls)
        
        links_list = ['link_about', 'link_services', 'link_platforms', 'link_works']   
        links_dict = {} 
        
        for link in links_list:
            links_dict[link] = []
                
        for url in urls:
            #print(link['href'])
            if 'about' in url:
                print(url)
                links_dict['link_about'].append(url)
            if 'service' in url:
                links_dict['link_services'].append(url)
        #for url in urls:
            if 'platform' in url:
                links_dict['link_platforms'].append(url)
                print(url)
            if 'works' in url:
                links_dict['link_works'].append(url)
        
        return links_dict
    
    def scrapping_data(self, links_dict):
        soup_about = ""
        soup_services = ''
        soup_platform = ''
        soup_works = ''
        for keys in links_dict.keys():
            print(links_dict[keys][0])
            if keys == 'link_about':
                soup_about = self.scrapping(links_dict[keys][0])

            if keys == 'link_services':
                soup_services = self.scrapping(links_dict[keys][0])

            if keys == 'link_platform':
                soup_platform = self.scrapping(links_dict[keys][0])

            if keys == 'link_works':
                soup_works = self.scrapping(links_dict[keys][0])
                
        return soup_about, soup_services, soup_platform, soup_works
    
    def extracting_p_tags(self, soup_about, soup_services, soup_platform, soup_works):
        soup_about = soup_about.find_all('p')
        soup_services = soup_services.find_all('p')
        #soup_platform = soup_platform.find_all('p')
        soup_works = soup_works.find_all('p')
        
        soup_about_p = ""        
        for s in soup_about:
            if len(s) == 0:
                continue
            #print(s.contents[0])
            soup_about_p = soup_about_p + '\n' + str(s.contents[0])
            
        
        soup_services_p = ""
        for s in soup_services:
            if len(s) == 0:
                continue
            #print(s.contents[0])
            soup_services_p = soup_services_p + '\n' + str(s.contents[0])
            
        
# =============================================================================
#         soup_platform_p = ""
#         for s in soup_platform:
#             if len(s) == 0:
#                 continue
#             #print(s.contents[0])
#             soup_platform_p = soup_platform_p + '\n' + str(s.contents[0])
#         
# =============================================================================
        soup_works_p = ""
        for s in soup_works:
            if len(s) == 0:
                continue
            #print(s.contents[0])
            soup_works_p = soup_works_p + '\n' + str(s.contents[0])
                
                
        return soup_about_p, soup_services_p, soup_works_p
        
    
def main():
    obj = scrape("https://www.lftechnology.com/")
    soup = obj.scrapping(obj.url)
    links = obj.get_links(soup)
    links_dict = obj.separate_links(links)
#    soup1 = obj.scrapping_data(links_dict)
    
    soup_about, soup_services, soup_platform, soup_works = obj.scrapping_data(links_dict)
    
    unnessary_links = soup_about.find_all(class_ = "fa fa-phone")   
    unnessary_links.append(soup_about.find_all(href = "tel:+81-0368032502")[0])  
    unnessary_links.append(soup_about.find_all(href = "tel:+977-15260714")[0])   
    unnessary_links.append(soup_about.find_all(href = "tel:+01-8178034169")[0])   
    unnessary_links.append(soup_about.find_all(href = "tel:+65-64921509")[0])   

    for links in unnessary_links:
        links.decompose()
        
        
    soup_a_p = obj.extracting_p_tags(soup_about, soup_services, soup_platform, soup_works)
    print(soup_a_p)
    
    soup_about_p, soup_services_p, soup_works_p = obj.extracting_p_tags(soup_about, soup_services, soup_platform, soup_works)
    
    soup_about_summarize = summarizer.summarize(soup_about_p)
    soup_about_keywords = keywords.keywords(soup_about_p)
    print(soup_about_summarize)
    print(soup_about_keywords)
    
    soup_services_summarize = summarizer.summarize(soup_services_p)
    soup_services_keywords = keywords.keywords(soup_services_p)
    print(soup_services_summarize)
    print(soup_services_keywords)
    
    soup_works_summarize = summarizer.summarize(soup_works_p)
    soup_works_keywords = keywords.keywords(soup_works_p)
    print(soup_works_summarize)
    print(soup_works_keywords)
    
    
    
 
text = """Automatic summarization is the process of reducing a text document with a
computer program in order to create a summary that retains the most important points
of the original document. As the problem of information overload has grown, and as
the quantity of data has increased, so has interest in automatic summarization.
Technologies that can make a coherent summary take into account variables such as
length, writing style and syntax. An example of the use of summarization technology
is search engines such as Google. Document summarization is another."""

from summa import summarizer
from summa import keywords
print(summarizer.summarize(soup_a_p))
print(keywords.keywords(soup_a_p))

'Automatic summarization is the process of reducing a text document with a computer
program in order to create a summary that retains the most important points of the
original document.'