#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:47:32 2018

@author: abhiyush
"""

import pandas as pd
import nltk
import re

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

f = open('/home/abhiyush/mPercept/Web crawling/Mpercept.txt', 'r')
Mpercept = f.read()
f.close()

print(Mpercept)

# Custom sentence tokenization
sentences_custom = re.split(r'[.?/\n]+', Mpercept) 
len(sentences_custom)

# Sentence tokenization using nltk
sentences = nltk.sent_tokenize(Mpercept)
print(sentences)
type(sentences)
len(sentences)
sentences[18]

df = pd.DataFrame(sentences, columns = ['Sentences'])


lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def preprocessing_lemmatizer(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = sentence.lower()
    sentence = sentence.split()
    sentence = [lemmatizer.lemmatize(word) for word in sentence]
    sentence = ' '.join(sentence)
    return sentence

def preprocessing_stemmer(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = sentence.lower()
    sentence = sentence.split()
    sentence = [ps.stem(word) for word in sentence]
    sentence = ' '.join(sentence)
    return sentence

df['sent_preprocess_lemmatizer'] = df['Sentences'].apply(preprocessing_lemmatizer)
df['sent_preprocess_stemmer'] = df['Sentences'].apply(preprocessing_stemmer)

def calculate_jaccard_similarity(sentence_train, sentence_test):
    train_words = []
    test_words = []
    
    train_words = [word for word in nltk.word_tokenize(sentence_train)]

    test_words_df = pd.DataFrame([sentence_test])
    test_words = test_words_df[0].apply(preprocessing_stemmer)
    test_words = nltk.word_tokenize(str(test_words[0]))
    
    a = set(train_words)
    b = set(test_words)
    c = a.intersection(b)
    return float(len(c) / (len(a) + len(b) - len(c)))

def chatbot_answer(sentence_test):
    high_jaccard_score = 0
    score = 0
    
    for sentence_train, sentence_train_stem in zip(df['Sentences'],df['sent_preprocess_stemmer']):
        #print(sentence_train)
        score = calculate_jaccard_similarity(sentence_train_stem, sentence_test)    
        
        if score > high_jaccard_score:
            high_jaccard_score = score
            answer = sentence_train
    return answer, high_jaccard_score



# =============================================================================
# sentence_test = "Tell me about Mpercept technology company?"
# sentence_test = "what is mpercept technology"
# sentence_test = "Areas of score"
# sentence_test = "What are the areas covered by Mpercept"
# sentence_test = "What are the areas covered?"
# sentence_test = "areas cover?"
# sentence_test = "location"
# sentence_test = "Where is mpercept located"
# sentence_test = "Email"
# sentence_test = "Can you tell me Email?"
# sentence_test = "What courses do you offer?"
# sentence_test = "Who are the founders of Mpercept? "
# sentence_test = "founders?"
# sentence_test = "founders?"
# =============================================================================


print("Ask a question:")
sentence_test = input()
answer, score = chatbot_answer(sentence_test)
print("\n" + answer)
print(score)

