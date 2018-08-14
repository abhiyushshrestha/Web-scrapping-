#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:51:04 2018

@author: abhiyush
"""
import pandas as pd
import nltk
import re

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from mpercept_scrapping_using_class import main

homepage_section = main()

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
corpus = []
def preprocessing_lemmatizer(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = sentence.lower()
    sentence = sentence.split()
    sentence = [lemmatizer.lemmatize(word) for word in sentence]
    sentence = ' '.join(sentence)
    corpus.append(sentence)
    return sentence, corpus

def preprocessing_stemmer(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = sentence.lower()
    sentence = sentence.split()
    sentence_tokenize = [ps.stem(word) for word in sentence]
    sentence = ' '.join(sentence)
    corpus.append(sentence)
    return sentence #, sentence_tokenize, corpus

homepage_section_word_tokenize = {}
for keys,values in zip(homepage_section.keys(),homepage_section.values()):
    homepage_section_word_tokenize[keys] = preprocessing_stemmer(values[0])
    homepage_section_word_tokenize[keys] = nltk.word_tokenize(homepage_section_word_tokenize[keys])

homepage_section_sentence_tokenize = {}
for keys, values in zip(homepage_section.keys(),homepage_section.values()):
    homepage_section_sentence_tokenize[keys]  = nltk.sent_tokenize(values[0])
    

def calculate_jaccard_similarity(sentence, class_name):
    test_word = []
    for word in nltk.word_tokenize(sentence):
        test_word.append(ps.stem(word).lower())
    a = set(test_word) 
    b = set(homepage_section_word_tokenize[class_name])
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def classify(sentence):
    high_jaccard_score = 0
    high_class = None
    score = 0
    
    for class_name in homepage_section_word_tokenize.keys():
        score = calculate_jaccard_similarity(sentence, class_name)
        
        if(score > high_jaccard_score):
            high_jaccard_score = score
            high_class = class_name
            
    return high_class, high_jaccard_score

classify("Mpercept technology")
classify("What is mpercept technology")
classify("Tell me about mpercept technology company")
classify("about mpercept technology")
classify("who are the founders?")
classify("What are the services provided?")




# =============================================================================
# 
# homepage_section_tfidf = {}
# for keys, values in zip(homepage_section.keys(), homepage_section.values()):
#     a,homepage_section_tfidf[keys],c = preprocessing_stemmer(values[0])
#     a,b,c = preprocessing_stemmer(values[0])
# 
# homepage_section_df = pd.DataFrame(homepage_section)
# homepage_section_df.info()
# homepage_section_df_preprocess = homepage_section_df.apply(preprocessing_stemmer)
# homepage_section_df["Info"][0]
# =============================================================================
