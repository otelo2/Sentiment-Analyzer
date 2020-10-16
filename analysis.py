from textblob import TextBlob
import json

with open('python.json', 'r') as f:
        line = f.readline()
        tweet = json.loads(line)
    #print(json.dumps(tweet, indent=4))

print(tweet["text"])
processedTweet = tweet["text"].replace("RT","").replace("@","")
print(processedTweet)
analysis = TextBlob(processedTweet)
analysis = analysis.translate(to='en')

#print(analysis.translate(to='en'))
print(analysis.sentiment)
