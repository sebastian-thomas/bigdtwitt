import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def calculateSentiment(tweet):
    terms = tweet.split()
    global termsFreq
    for term in terms :
        if term[0] == '#':
            if term in termsFreq.keys():
                termsFreq[term] +=1
            else:
                termsFreq[term] = 1
        
    
    

def main():
    tweet_file = open(sys.argv[1])
    global termsFreq
    for l in tweet_file:
    	lineJson = json.loads(l)
    	if 'entities' in lineJson.keys() :
            #print "entityyyyy"
            entity = lineJson["entities"]
            if 'hashtags' in entity.keys():
                hashtags = entity['hashtags']
                for tag in hashtags:
                    if tag['text'] in termsFreq.keys():
                        termsFreq[tag['text']] +=1
                    else:
                        termsFreq[tag['text']] =1
    sortedx = sorted(termsFreq.iteritems(),  key=operator.itemgetter(1),reverse=True)
    for i in range(10):
        term = sortedx[i]
        print str(term[0]) + " "+str(float(term[1]))

    	   

termsFreq = {}
totalTerms = 0
if __name__ == '__main__':
    main()
