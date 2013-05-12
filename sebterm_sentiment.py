import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def calculateSentiment(tweet , scores):
    terms = tweet.split()
    tscore = 0
    countTerms=0
    for term in terms :
        if term in scores.keys():
            ts = scores[term]
            countTerms += 1
        else:
            ts = 0
        tscore += ts
    if countTerms == 0 :
    	countTerms = 1
    for term in terms :
    	if term not in scores.keys():
    		if term in termstofindscore.keys():
    			termstofindscore[term] += termstofindscore[term] + tscore/countTerms
    			termsfrequency[term] += 1
    		else:
    			termstofindscore[term] =  tscore/countTerms
    			termsfrequency[term] = 1


    

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
    for term in termstofindscore :
    	print term +" "+str(termstofindscore[term])
    	#print type(termstofindscore[term])



termstofindscore = {}
termsfrequency = {}
if __name__ == '__main__':
    main()
