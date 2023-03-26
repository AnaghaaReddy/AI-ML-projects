# -*- coding: utf-8 -*-
"""SENTIMENT_ANALYSIS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aXE03-h7z8j7ukrUSwoZwSWwl_fDaWFC
"""

!pip install nltk
!pip install textblob
!pip install newspaper3k

import nltk
nltk.download('punkt')

from textblob import TextBlob
from newspaper import Article

url='https://www.thefirstnews.com/article/the-horrifying-story-of-hitlers-concentration-camp-for-children-3622' 
article=Article(url)

article.download() #download article into script
article.parse() #to make article readable 
article.nlp()

text=article.summary
print(text) #complete text without html

blob=TextBlob(text)
sentiment=blob.sentiment.polarity #-1 negative 0 netural 1 positive
print("sentiment value",sentiment)

url1='https://quitpit.com/emilia-clarke-recovery-story/' 
article1=Article(url1)
article1.download() #download article into script
article1.parse() #to make article readable 
article1.nlp()
text1=article1.summary
print(text1)
blob1=TextBlob(text1)
sentiment1=blob1.sentiment.polarity #-1 negative 0 netural 1 positive
print("sentiment value",sentiment1)

url2='https://www.who.int/news-room/feature-stories/detail/the-impact-of-covid-19-on-mental-health-cannot-be-made-light-of' 
article2=Article(url2)
article2.download() #download article into script
article2.parse() #to make article readable 
article2.nlp()
text2=article2.summary
print(text2)
blob2=TextBlob(text2)
sentiment2=blob2.sentiment.polarity #-1 negative 0 netural 1 positive
print("sentiment value",sentiment2)