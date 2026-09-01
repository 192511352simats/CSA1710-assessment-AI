from textblob import TextBlob

text = input("Enter a sentence: ")

score = TextBlob(text).sentiment.polarity

if score > 0:
    print("Sentiment: Positive")
elif score < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
