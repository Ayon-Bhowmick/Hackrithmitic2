import pandas as pd
import csv
import cohere
from sklearn.model_selection import train_test_split
# import SVM classifier code
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_20newsgroups

pd.set_option('display.max_colwidth', None)

# Get the SST2 training and test sets
df_train = pd.read_csv('https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv', delimiter='\t', header=None)

# Let's glance at the dataset
df_train.head()

# Set the number of examples from the dataset
num_examples = 200
# Create a dataframe that
df_sample = df_train.sample(num_examples)


# Split into training and testing sets
sentences_train, sentences_test, labels_train, labels_test = train_test_split(
            list(df_sample[0]), list(df_sample[1]), test_size=0.25, random_state=0)



# ADD YOUR API KEY HERE
api_key = "qjXHW7uXtFQR6Nz5Qml8L2oODO7CYUMxksGN331r"

# Create and retrieve a Cohere API key from dashboard.cohere.ai
co = cohere.Client(api_key)

# Embed the training set
embeddings_train = co.embed(texts=sentences_train,
                             model="large",
                             truncate="LEFT").embeddings
# Embed the testing set
embeddings_test = co.embed(texts=sentences_test,
                             model="large",
                             truncate="LEFT").embeddings

# Here we are using the endpoint co.embed()

# print(f"\n\nReview text: {sentences_train[0]}")
# print(f"Embedding vector: {embeddings_train[0][:10]}")

# Initialize a support vector machine, with class_weight='balanced' because
# our training set has roughly an equal amount of positive and negative
# sentiment sentences
svm_classifier = make_pipeline(StandardScaler(), SVC(class_weight='balanced'))

# fit the support vector machine
svm_classifier.fit(embeddings_train, labels_train)

# get the score from the test set, and print it out to screen!
score = svm_classifier.score(embeddings_test, labels_test)
# print(f"Validation accuracy on Large is {100*score}%!")
# run the model on one one phrase
# print(embeddings_test[0])
embed_test = co.embed(["I love this airline!"])
print(svm_classifier.predict(embed_test))
