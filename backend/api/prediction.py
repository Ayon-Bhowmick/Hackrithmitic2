from textblob import TextBlob
# Get the text from user input
text = input("Enter a sentence: ")

# Get the sentiment of the text
sentiment = TextBlob(text).sentiment.polarity
print(sentiment)
# Print the sentiment
if sentiment > 0:
    print("Positive")
else:
    print("Negative")