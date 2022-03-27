#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#search list for reading search terms 
searchList = []
with open("Search-terms.txt","r") as f:
    for item in f:
        searchList.append(item.lower().strip("\n"))

#Variables that contains the user credentials to access Twitter API 
access_token = "493775154-8X63gMqY6SZ1OHp7NaRmtBGoV5fYF5Ceyklic6vW"
access_token_secret = "pKKsWvcfFD9prX5oqDPcWaDRQW7k5t1aE9rcQFYq38XCV"
consumer_key = "Kob2hJ4huaB71tgHpa0Txu6jd"
consumer_secret = "yIYiGFqf7L1DucYlstWNbQmZqtcY0pVNjqtMzrRCIAvvBKBnnJ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'cancer'
    stream.filter(track=searchList)