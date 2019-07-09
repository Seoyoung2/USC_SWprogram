import tweepy

consumer_key = 'hhfzCiaNAgaZDFsaL6KGUesz2'
consumer_secret = 'W6N7OxArLj6tYV8Dh8XajwitIuWYCRd0pmWu1jOHJvUzBVqiln'

access_token = '1059208697010782208-zXq2crexkA95x63uPiACoN4zbuakiw'
access_token_secret = 'EOIhSkiESdve1azNTIrFfJY2ZJ9e0hNbnVIoZGCTb1Cfw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# fetch_tweets = tweepy.Cursor(api.search, q='Trump').items(5)

# for i in fetch_tweets:
#     print('----')
#     print(i)
#     print(i.text)       
#     print('----')

fetch_tweets = tweepy.Cursor(api.search, q='Korea').items(5)

for tweet_rec in fetch_tweets:
    print('----')
    
    print('Tweet ID:' + str(tweet_rec.id))
    print('Tweet Text: ' + tweet_rec.text.replace('\n', ''))
    print('Tweet Created At: ' + str(tweet_rec.created_at))
    print('Tweet Coordinates: ' + str(tweet_rec.coordinates))
    
    print('User ID: ' + str(tweet_rec.user.id))
    print('User Screen Name: ' + tweet_rec.user.screen_name)
    print('User Name: ' + tweet_rec.user.name)
    print('User Location: ' + str(tweet_rec.user.location))
    
    print('Retweet Count: ' + str(tweet_rec.retweet_count))
    print('Retweeted: ' + str(tweet_rec.retweeted))
    print('Phone Type: ' + str(tweet_rec.source))
    print('Favorite Count: ' + str(tweet_rec.favorite_count))
    print('Favorited: ' + str(tweet_rec.favorited))
    print('Replied: ' + str(tweet_rec.in_reply_to_status_id_str))
                    
    print('----')

# fetch_tweets2 = tweepy.Cursor(api.search, q='Trump', geocode="34.052235,-116.243683,100km").items(10)

# for i in fetch_tweets2:
#     print('----')
#     print(i)
#     print(i.id)
#     print(i.text)
#     print(i.user.id)
#     print(i.user.screen_name)      
#     print('----')
