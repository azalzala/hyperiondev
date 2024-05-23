
# Load spaCy, pandas, textblob 
import pandas as pd
import spacy as sp
from textblob import TextBlob
# Load spaCy model 
nlp = sp.load('en_core_web_sm')

# Import data for sentiment analysis 
df = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# Investigate product review ratings for each category of product
df.groupby('categories')['reviews.rating'].describe()

# Segment data for sentiment analysis into new dataframe, drop reviews with no text or rating
reviews = df[['reviews.rating','reviews.text']].dropna(subset=['reviews.text'])

# This code performs 3 tasks: 
    # it cleans the text data
    #it identifies the sentiment polarity of the text and classifies the sentiment
    # it returns the similarity between two reviews 

# Pre-process review text using spaCys NLP model parser, tokenizer, lemmatizer parameters to remove stopwords and punctuation
def preprocess(text): 
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# Process review.text to generate a column for sentiment analysis titled 'processed_review'
reviews['processed_review'] = reviews['reviews.text'].apply(preprocess)

# Return sentiment polarity for each review using Textblob 
def get_sentiment(review):
    blob = TextBlob(review) #Process the input using Textblob to generate a polarity, subjectivity tuple 
    sentiment = blob.sentiment.polarity 
    return sentiment # Output the polarity score 

# Apply the function to return a sentiment score for each review
reviews['sentiment'] = reviews['processed_review'].apply(get_sentiment)

# Classify the sentiment polarity into one of three groups: negative, neutral or positive 
def classify_sentiment(sentiment):
# If the sentiment is larger than 0, output should be "positive"
    if sentiment > 0: 
        return "positive"
    elif sentiment < 0: 
        return 'negative'
    else: 
# If the sentiment is zero, output should be "neutral"
        return 'neutral'
        
# Apply the function to classify sentiment for each review
reviews['sentiment_class']= reviews['sentiment'].apply(classify_sentiment)
print(reviews['sentiment_class'].unique())

# Assign two reviews as input for the similarity function  
review1 = reviews['processed_review'][4]
review2 = reviews['processed_review'][78]

# Using the spacy property, output the similarity between the two reviews 
def similarity(review1, review2): 
    return nlp(review2).similarity(nlp(review1)) 

# Store the similarity score as a variable 
similarity_score = similarity(review1, review2)

print(f"The similarity between these reviews is {similarity_score}")

test_review = reviews['processed_review'][7]

sentiment_test = get_sentiment(test_review)
sentiment_class_test = classify_sentiment(test_review)
print(f"The review 6 is {sentiment_test} and is classified as {sentiment_class_test}")