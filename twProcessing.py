import json
from nltk.tokenize import word_tokenize
from collections import Counter

with open('twitter@realDonaldTrump.txt', 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        tokens = word_tokenize(tweet['text'].lower())
        print tokens