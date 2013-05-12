import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def calculateSentiment(tweet , scores, place):
    terms = tweet.split()
    tscore = 0
    global stateval
    for term in terms :
        if term in scores.keys():
            ts = scores[term]
        else:
            ts = 0
        tscore += ts
    if place in stateval.keys():
        if stateval[place] < tscore :
            stateval[place] = tscore
    else:
        stateval[place] = tscore
    #print tscore
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores ={}
    global state
    for line in sent_file:
    	term , score = line.split("\t")
    	scores[term] = int(score)
    for l in tweet_file:
    	lineJson = json.loads(l)
    	if 'text' in lineJson.keys() :
            if lineJson['place'] !=  None :
                if lineJson['place']['name']!= None :
                    if lineJson['place']['name'].upper() in state.keys() :
                        calculateSentiment(lineJson['text'], scores ,lineJson['place']['name'])
    happy = 'Alabama'
    happyv=-5

    for k,v in stateval.items():
        if v > happyv:
            happy = k
            happyv = v

    print state[happy.upper()]

    	   
          
           
            

    	   

stateval ={}
state = {
'ALABAMA':'AL',
'ALASKA':'AK',
'AMERICAN SAMOA':'AS',
'ARIZONA':'AZ',
'ARKANSAS':'AR',
'CALIFORNIA':'CA',
'COLORADO':'CO',
'CONNECTICUT':'CT',
'DELAWARE':'DE',
'DISTRICT OF COLUMBIA':'DC',
'FEDERATED STATES OF MICRONESIA':'FM',
'FLORIDA':'FL',
'GEORGIA':'GA',
'GUAM GU':'GU',
'HAWAII':'HI',
'IDAHO':'ID',
'ILLINOIS':'IL',
'INDIANA':'IN',
'IOWA':'IA',
'KANSAS':'KS',
'KENTUCKY':'KY',
'LOUISIANA':'LA',
'MAINE':'ME',
'MARSHALL ISLANDS':'MH',
'MARYLAND':'MD',
'MASSACHUSETTS':'MA',
'MICHIGAN':'MI',
'MINNESOTA':'MN',
'MISSISSIPPI':'MS',
'MISSOURI':'MO',
'MONTANA':'MT',
'NEBRASKA':'NE',
'NEVADA':'NV',
'NEW HAMPSHIRE':'NH',
'NEW JERSEY':'NJ',
'NEW MEXICO':'NM',
'NEW YORK':'NY',
'NORTH CAROLINA':'NC',
'NORTH DAKOTA':'ND',
'NORTHERN MARIANA ISLANDS':'MP',
'OHIO':'OH',
'OKLAHOMA':'OK',
'OREGON':'OR',
'PALAU':'PW',
'PENNSYLVANIA':'PA',
'PUERTO RICO':'PR',
'RHODE ISLAND':'RI',
'SOUTH CAROLINA':'SC',
'SOUTH DAKOTA':'SD',
'TENNESSEE':'TN',
'TEXAS':'TX',
'UTAH':'UT',
'VERMONT':'VT',
'VIRGIN ISLANDS':'VI',
'VIRGINIA':'VA',
'WASHINGTON':'WA',
'WEST VIRGINIA':'WV',
'WISCONSIN':'WI',
'WYOMING':'W'}

if __name__ == '__main__':
    main()
