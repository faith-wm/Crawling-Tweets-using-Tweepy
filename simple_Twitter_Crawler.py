
import tweepy
import csv

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')   #enter authentication details based on your twitter account--
                                                            #read here how to get them https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth,wait_on_rate_limit=True)

saveFilename='xxxx.csv'
searchTerms=["virus"]  #keywords/ search terms

index=0
for term in searchTerms:
    for tweet in tweepy.Cursor(api.search,q =term,lang = "en").items(10000):  #since="2010-01-01",until="2019-12-04"
        index+=1
        print('extracted tweets so far {}'.format(index))

        tweet_id = tweet.id_str
        user_id = tweet.user.id
        user_name = tweet.user.name
        date = tweet.created_at
        location = tweet.user.location
        retweet_count = tweet.retweet_count
        text = tweet.text

        my_dict={index:[tweet_id,user_id,user_name,date,location,retweet_count,text]}
        with open(saveFilename, 'a') as outfile:
            writer = csv.writer(outfile)
            for k, v in my_dict.items():
                writer.writerow([k] + v)

