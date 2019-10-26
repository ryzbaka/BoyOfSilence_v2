import json
from flask import Flask,render_template
import time
import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import sys 
###API AUTHORIZATION###
consumer_key="Ee0lw604kCAuzTbFp3pcn5lck"
consumer_secret="uuedTNbrDhmhsI8QBeOeCcEaOxtoe4nXDPDcRd8XkLF67yzjQ1"

access_token="857652506079490048-pPDneGr61On9KS4KQ5yWG4wHZCvvdMz"
access_token_secret="kZEayyj3UM56Lf9xkk10yNgr8wCod6JXgnu0BueKcN5f7"


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
#######################
#####ROUTING#####
app=Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route("/")
@app.route("/<message>")
def get_homepage(message="nothing"):
    return render_template('index.html',message=message)

@app.route("/something<name>")
def return_something(name):    
    object=json.dumps({'message':name})
    return object

@app.route("/sentiment<keyword>")
def return_sentiment(keyword):
    public_tweets=api.search(keyword)
    sentiment=0
    subjectivity=0
    for tweet in public_tweets:
        analysis=TextBlob(tweet.text)
        sentiment+=analysis.sentiment[0]
        subjectivity+=analysis.sentiment[1]
    object={'sentiment':round(sentiment,2),'status':'okay'}
    json_object=json.dumps(object)
    return json_object

#################
app.run(port=5500)

'''

def get_sentiment(search_string):
    public_tweets=api.search(search_string)
    count=0
    sentiment=0
    subjectivity=0
    for tweet in public_tweets:
        analysis=TextBlob(tweet.text)
        sentiment+=analysis.sentiment[0]
        subjectivity+=analysis.sentiment[1]
    return {'sentiment':sentiment,'subjectivity':subjectivity}
'''