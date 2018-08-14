#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:38:00 2018

@author: abhiyush
"""

import requests
from bs4 import BeautifulSoup

# Scraping the data from mpercept.com

url = 'http://mpercept.com/'

page = requests.get(url)
page.text

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

website_title = soup.find_all(class_ = "section-title")
type(website_title)
for title in website_title:
    if title.contents[0] == 'About Us':
        print("About us\n")
   
        id_about = soup.find(id = "about")
        id_about_section_desc = id_about.find('p')
        print(id_about_section_desc.contents[0])
        about_us = title.contents[0] + "\n" + id_about_section_desc.contents[0]
    if title.contents[0] == "Areas We Cover":
        print("\n\nAreas We Cover\n")
        areas_cover = ""
        id_areas_we_cover = soup.find(id = "features")
        id_areas_we_cover_desc = id_areas_we_cover.find_all('a')
        for areas in id_areas_we_cover_desc:
            if len(areas) != 0:
                print(areas.contents[0]) 
                areas_cover = areas_cover + areas.contents[0] + "\n"
        areas_we_cover = title.contents[0] +"\n" + areas_cover  
        
    if title.contents[0] == "Our Services":   
        print("\n\nOur Services\n")
        services = ''
        id_our_services = soup.find(id = "advanced-features")
        id_our_services_head = id_our_services.find_all('h2')
        id_our_services_desc = id_our_services.find_all('p')
        
        i = 0
        for heading in id_our_services_head:
            print("\n\n" + heading.contents[0] + "\n")
            desc_list = []
            
            for desc in id_our_services_desc:
                desc_list.append(str(desc.contents[0]))     
            print(desc_list[i])
            services = services +"\n" + heading.contents[0] + "\n" + str(desc_list[i]) +"\n"
            #print(services)
            i = i + 1
        our_services = title.contents[0] + "\n" + services               
            
    if title.contents[0] == "Founders":   
        print("Founders\n")    
        founders = ""
        id_founder = soup.find(id = "team")
        id_founder_name = id_founder.find_all('h4')
        for name in id_founder_name:
            print(name.contents[0])
            founders = founders + "\n" + name.contents[0]
        founders = title.contents[0] + "\n" + founders
    if title.contents[0] == "Portfolio":   
        print("\nPortfolio\n") 
        portfolio = ""
        id_portfolio = soup.find(id = "clients")
        id_portfolio_desc = id_portfolio.find_all('p')
        for desc in id_portfolio_desc:
            print(desc.contents[0])
            portfolio = portfolio + "\n" + desc.contents[0]
        portfolio = title.contents[0] + "\n" + portfolio
        print(portfolio)
print("Mpercept info\n")
info = soup.find(class_ = "contact-about")
info = info.find('p')
info = info.contents[0]
info = "Mpercept\n" + info

print(info)

print("Mpercept contact/n")
contact_info = soup.find(class_ = "info_contact")
contact_info = contact_info.find_all('p')

contact_info_list = []
for contacts in contact_info:
    contact_info_list.append(contacts.contents[0])
    
location = "Location\n" + contact_info_list[0]
email = "Email\n" + contact_info_list[1]   

Mpercept = ''
Mpercept = about_us + areas_we_cover + our_services + founders + "\n\n" + portfolio + info + "\n" + location + "\n\n" +email

print(Mpercept)

f = open('/home/abhiyush/mPercept/Web crawling/Mpercept.txt', 'w')
f.write(Mpercept)
f.close()
        
