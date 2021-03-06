from TwitterSearch import *
import time
import os
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['']) # 
#    tso.addKeywords(['#DolarBlue']) # let's define all words we would like to have a look for
#    tso.setLanguage('en') # we want to see German tweets only
#    tso.setLocale('en')
    tso.setResultType('recent')
#    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )

    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
        data = (( '@%s %s %s'  % ( tweet['user']['screen_name'], tweet['created_at'], tweet['text'] ) ).replace("\n", "").encode('ascii', 'ignore'))
        time.sleep(0.1)
        print data
        print ''
        saveFile = open('twitDB.csv','a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()
        
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
