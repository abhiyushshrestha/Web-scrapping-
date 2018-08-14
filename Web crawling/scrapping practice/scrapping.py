#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:46:22 2018

@author: abhiyush
"""
# To scrape the data of brickset.com using scrapy

import scrapy 

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls =  ["http://brickset.com/sets/year-2016"]
    
    def parse(self, response):
        SET_SELECTOR = '.set'
        
        for brickset in response.css(SET_SELECTOR):
            #NAME_SELECTOR = 'h1 a ::text'
            NAME_SELECTOR = './/h1/a/text()'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                        'name' : brickset.xpath(NAME_SELECTOR).extract_first(),
                        'pieces' : brickset.xpath(PIECES_SELECTOR).extract_first(),
                        'minifigs' : brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                        'image' : brickset.css(IMAGE_SELECTOR).extract_first(),
                    }
        
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
 
        if next_page:
            yield scrapy.Request(
                    response.urljoin(next_page),
                    callback = self.parse
                )
        
        NEXT_YEAR_SELECTOR = '.browselinks .col:last-child a ::attr(href)'
        next_year = response.css(NEXT_YEAR_SELECTOR).extract_first()
        
        if next_year:
            yield scrapy.Request(
                        response.urljoin(next_year),
                        callback = self.parse
                    )
       
        
        