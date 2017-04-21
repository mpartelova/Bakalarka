import json
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#from nltk.tokenize import RegexpTokenizer
from collections import Counter

out = open('trumpsentiment.csv','w')
out.write(", neg, neutral, pos, compound, retweet\n")
with open('twitter@realDonaldTrump.txt', 'r') as f:
    count_all = Counter()
    #tokenizer = RegexpTokenizer(r'\w+')
    vader_analyzer = SentimentIntensityAnalyzer()
    ind = 1


    for line in f:
        tweet = json.loads(line)
        tweet['text'] = re.sub(r'http.*?\s','', tweet['text']) #odstranenie url zo stredu textu
        tweet['text'] = re.sub(r'http.*?\Z','', tweet['text']) #odstranenie url z konca tweetu
        tweet['text'] = re.sub(r'@.*?\s','', tweet['text']) #odstranenie usera z tweetu
        tweet['text'] = re.sub(r'[^\w,\s]','', tweet['text']) #odstranenie usera z tweetu
        tokens = tweet['text'].lower()
        #print(tweet)
        #tokens = tokenizer.tokenize(tweet['text'].lower())
        out.write(str(ind)+ ", " + ', '.join(map(str,vader_analyzer.polarity_scores(tweet['text']).values())) + ", " + str(tweet['retweet_count']) + "\n")
        ind += 1
        #count_all.update(tokens)
        #break
    #print(count_all.most_common(5))
out.close()