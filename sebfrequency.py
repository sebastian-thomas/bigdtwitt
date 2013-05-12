import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def calculateSentiment(tweet):
    terms = tweet.split()
    global totalTerms
    global termsFreq
    for term in terms :
        if term in termsFreq.keys():
            termsFreq[term] +=1
        else:
            termsFreq[term] = 1
        totalTerms +=1
    
    

def main():
    tweet_file = open(sys.argv[1])
    global totalTerms
    global termsFreq
    for l in tweet_file:
    	lineJson = json.loads(l)
    	if 'text' in lineJson.keys() :
    	   calculateSentiment(lineJson['text'])  
    for term in termsFreq:
        print term +" "+str (termsFreq[term] / float(totalTerms))

    	   

termsFreq = {}
totalTerms = 0
if __name__ == '__main__':
    main()
