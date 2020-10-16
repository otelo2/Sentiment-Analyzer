from textblob import TextBlob
import json

with open('python.json', 'r') as f:
        line = "a"
        if line:
            while line:
                #Load tweet from JSON
                line = f.readline()
                tweet = json.loads(line)
                #Remove RT and @
                processedTweet = tweet["text"].replace("RT","").replace("@","")
                print(processedTweet)
                #Start processing
                analysis = TextBlob(processedTweet)
                if analysis.detect_language() != 'en':
                    analysis = analysis.translate(to='en')
                #print results
                print(analysis)
                print(analysis.sentiment)
                print("\n")

# #print(analysis.translate(to='en'))
# print(analysis.sentiment)
#     #print(json.dumps(tweet, indent=4))

# print(tweet["text"])
# processedTweet = tweet["text"].replace("RT","").replace("@","")
# print(processedTweet)
# analysis = TextBlob(processedTweet)
# analysis = analysis.translate(to='en')

# #print(analysis.translate(to='en'))
# print(analysis.sentiment)
