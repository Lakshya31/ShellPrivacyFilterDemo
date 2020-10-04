from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from string import digits
import csv
import glob
import os
import re
import numpy as np 
import pandas as pd

emails_df = pd.read_csv('data/sample.csv')
print(emails_df.shape)

mails = emails_df["content"].tolist()
print(mails)

with open('sample_vader.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for line in mails:
        # Strips the newline character 
        line.replace('\t', '')
        line.replace('\n', '')
        remove_digits = str.maketrans('', '', digits)
        sentence = line.translate(remove_digits)
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(line) 
        #print(sentence)
        s=0
        if sentiment_dict['compound'] >= 0.05 : 
            #"Positive" 
            s=0
        elif sentiment_dict['compound'] <= - 0.05 : 
            #"Negative" 
            s=2
        else : 
            #"Neutral"
            s=1
        writer.writerow([line, sentiment_dict['pos'], sentiment_dict['neu'], sentiment_dict['neg'], sentiment_dict['compound'], s])