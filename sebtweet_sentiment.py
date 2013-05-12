import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def calculateSentiment(tweet , scores):
    terms = tweet.split()
    tscore = 0
    for term in terms :
        if term in scores.keys():
            ts = scores[term]
        else:
            ts = 0
        tscore += ts
    print tscore
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores ={}
    for line in sent_file:
    	term , score = line.split("\t")
    	scores[term] = int(score)
    for l in tweet_file:
    	lineJson = json.loads(l)
    	if 'text' in lineJson.keys() :
    	   calculateSentiment(lineJson['text'], scores )    	
    	   


if __name__ == '__main__':
    main()
