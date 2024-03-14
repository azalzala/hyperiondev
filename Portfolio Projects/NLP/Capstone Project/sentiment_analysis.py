
# Load spaCy small model, pandas, numpy 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import spacy as sp
from textblob import TextBlob

# Import data 
df = pd.read_csv('/Users/ayazalzala/hyperiondev/1429_1.csv', usecols=['id', 'name', 'asins','categories', 'reviews.rating', 'reviews.text', 'reviews.title', 'reviews.username'], low_memory=False)

# Investigate product review ratings for each category of product
df.groupby('categories')['reviews.rating'].describe()

# Segment data for sentiment analysis into new dataframe, drop reviews with no text or rating
reviews = df[['reviews.rating','reviews.text']].dropna(subset=['reviews.text'])

# This programme performs x tasks: 
    # it cleans the text data
    #it identifies the sentiment polarity of the text and classifies the sentiment
    # it returns the similarity between two reviews 
     
# Pre-process review text using spaCys NLP model parser, tokenizer, lemmatizer parameters to remove stopwords and punctuation
def preprocess(text): 
    nlp = sp.load('en_core_web_sm')
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# Process review.text to generate a column for sentiment analysis titled 'processed_review'
reviews['processed_review'] = reviews['reviews.text'].apply(preprocess)

# Return sentiment polarity for each review using Textblob 
def get_sentiment(review):
    blob = TextBlob(review) 
    sentiment = blob.sentiment.polarity
    return sentiment

text = np.asarray(reviews['processed_review'])

# Classify the sentiment polarity into one of three groups: negative, neutral or positive 
for i, review in enumerate(text): 
    sentiment = get_sentiment(review)
    if sentiment > 0: 
        reviews['sentiment'] = "positive"
    elif sentiment < 0: 
        reviews['sentiment']= 'negative'
    elif sentiment == 0: 
        reviews['sentiment']= 'neutral'

# Apply the function to return a sentiment score for each review
reviews['sentiment']= reviews['processed_review'].apply(get_sentiment)

# Building the similarity function 
review1 = reviews['processed_review'][4]
review2 = reviews['processed_review'][78]

def similarity(review1, review2): 
    return nlp(review2).similarity(nlp(review1)) 

similarity_score = similarity(review1, review2)

print(f"The similarity between {review1} and {review2} is {similarity_score}")
