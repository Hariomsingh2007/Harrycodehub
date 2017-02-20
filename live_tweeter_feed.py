from __future__ import absolute_import, print_function
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from bs4 import BeautifulSoup
import json
import re

# Get the below Key from Twitter developer page.
consumer_key="" 
consumer_secret=""

access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        #print(data)
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        harry = json.loads(data)
        print(harry["created_at"])
        text=harry["text"]
        encoded = text.encode("utf-8", errors='ignore')
       
        #print(encoded)
        sentence=text_clensing(encoded)
        print(sentence)
        
        print("============================================================================")
        return True

    def on_error(self, status):
        print(status)

##harry unit to find the clean text
def text_clensing(a):
    new_str = a.decode("utf-8")
    filter(lambda x:x[0]!='@', new_str.split())
    result_temp1=" ".join(filter(lambda x:x[0]!='@', new_str.split()))
    filter(lambda x:x[0]!='#', result_temp1.split())
    result_temp2=" ".join(filter(lambda x:x[0]!='#', result_temp1.split()))
    pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    result=pattern.sub('', result_temp2)
    
    return result 
        
        

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['TimesNow'])
