import sys
import csv

import argparse
import tweepy
import pandas as pd
import logging
from textblob import TextBlob
import matplotlib.pyplot as plt



consumer_key = "8hGoSZ1qFew1XsdMnaAgNRZ9f"
consumer_secret = "HQK5BfW8OMDBEqEKMjRxzaLCcVF8BgPjNiG5eT0bXDiS1JC3Ro"
access_key = "2853255397-CUdDZnKtigKDF8BD26cdc9ncNNyBKJePYu7jfFz"
access_secret = "ue3esWfccJ6MWAPJIRUjCd4hnYMArQd6uP5xTT7GocvtA"

def getTweets(username,noOfTweets):
	"""
	parameter: 
		username - username of the twitter handle 
		noOfTweets - number of tweets we want to extract
	
	Get the tweets and save it in csv file.
	In current Working Directory
	"""
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name=username, count=noOfTweets)
	columns = ['User', 'Tweet ID', 'Date/Time', 'Text','Retweet', 'Followers_count', 'statuses_count', 'Polarity', 'Subjectivity', 'Sentiment_status']
	# columns = ['User', 'Tweet ID', 'Date/Time', 'Text','Retweet', 'Followers_count']
	if noOfTweets is None:
		tweets_for_csv = []
		for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items():
			###################### Retweet ##########################################				
			# getting the retweeters
			retweets_list = api.get_retweets(tweet.id_str)
			for retweet in retweets_list:
				retweet_names = retweet.user.screen_name


			##################### Followers_count ###########################################
			# the screen name of the user
			# screen_name = "PracticeGfG"
			  
			# fetching the user
			user = api.get_user(screen_name=username)
			  
			# fetching the followers_count
			followers_count = user.followers_count			  
			# print("The number of followers of the user are : " + str(followers_count))

			##################### Status_count ###########################################
			# fetching the statuses_count attribute
			statuses_count = user.statuses_count 
  
			# print("The number of statuses the user has posted are : " + str(statuses_count))
			############################## Sentimant analysis ##################################
			analysis = TextBlob(tweet.text)
			# print(analysis.sentiment)  # print tweet's polarity
			# print('Polarity: ', analysis.sentiment.polarity)
			# print('subjectivity: ', analysis.sentiment.subjectivity)
			polarity = analysis.sentiment.polarity
			if (polarity == 0):
				sentiment_status = 'Neutral'
				# print('sentiment_status',sentiment_status)
			elif (polarity > 0 and polarity <= 0.3):
				sentiment_status = 'Weakly Positive'
				# print('sentiment_status',sentiment_status)
			elif (polarity > 0.3 and polarity <= 0.6):
				sentiment_status = 'Positive'
				# print('sentiment_status',sentiment_status)
			elif (polarity > 0.6 and polarity <= 1):
				sentiment_status = 'Strongly Positive'
				# print('sentiment_status',sentiment_status)
			elif (polarity > -0.3 and polarity <= 0):
				sentiment_status = 'Weakly Negative'
				# print('sentiment_status',sentiment_status)
			elif (polarity > -0.6 and polarity <= -0.3):
				sentiment_status = 'Negative'
				# print('sentiment_status',sentiment_status)
			elif (polarity > -1 and polarity <= -0.6):
				sentiment_status = 'Strongly Negative'
				# print('sentiment_status',sentiment_status)
			################################### CSV Write ####################################
			tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), retweet.user.screen_name, followers_count, user.statuses_count, analysis.sentiment.polarity, analysis.sentiment.subjectivity, sentiment_status])

			# tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), retweet.user.screen_name, followers_count])
			
	else:
		tweets_for_csv = []
		for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(noOfTweets):			
			###################### Retweet ##########################################				
			# getting the retweeters
			retweets_list = api.get_retweets(tweet.id_str)

			for retweet in retweets_list:
				retweet_names = retweet.user.screen_name
			##################### Followers_count ###########################################
			# the screen name of the user
			# screen_name = "PracticeGfG"
			  
			# fetching the user
			user = api.get_user(screen_name=username)
			  
			# fetching the followers_count
			followers_count = user.followers_count
			  
			# print("The number of followers of the user are : " + str(followers_count))
			##################### Status_count ###########################################
			# fetching the statuses_count attribute
			statuses_count = user.statuses_count 
  
			# print("The number of statuses the user has posted are : " + str(statuses_count))
			############################## Sentimant analysis ##################################
			analysis = TextBlob(tweet.text)
			# print(analysis.sentiment)  # print tweet's polarity
			# print('Polarity: ', analysis.sentiment.polarity)
			# print('subjectivity: ', analysis.sentiment.subjectivity)
			polarity = analysis.sentiment.polarity
			if (polarity == 0):
				sentiment_status = 'Neutral'
				# print('sentiment_status',sentiment_status)
			elif (polarity > 0 and polarity <= 0.3):
				sentiment_status = 'Weakly Positive'
				# print('sentiment_status',sentiment_status)
			elif (polarity > 0.3 and polarity <= 0.6):
				sentiment_status = 'Positive'
				# print('sentiment_status',sentiment_status)
			elif (polarity > 0.6 and polarity <= 1):
				sentiment_status = 'Strongly Positive'
				# print('sentiment_status',sentiment_status)
			elif (polarity > -0.3 and polarity <= 0):
				sentiment_status = 'Weakly Negative'
				# print('sentiment_status',sentiment_status)
			elif (polarity > -0.6 and polarity <= -0.3):
				sentiment_status = 'Negative'
				# print('sentiment_status',sentiment_status)
			elif (polarity > -1 and polarity <= -0.6):
				sentiment_status = 'Strongly Negative'
				# print('sentiment_status',sentiment_status)
			################################### CSV Write ####################################
			tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), retweet.user.screen_name, followers_count, user.statuses_count, analysis.sentiment.polarity, analysis.sentiment.subjectivity, sentiment_status])
			# tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), retweet.user.screen_name, followers_count])



	df = pd.DataFrame(tweets_for_csv, columns=columns)
	# print(df)
	#Write the tweets list to csv file.
	fileName = username + "_tweets.csv"
	with open(fileName, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerow(columns)

		writer.writerows(tweets_for_csv)
	
	print('@'+username+" Tweets Save in "+fileName)

if __name__ == '__main__':
	"""
	Get the username and number of tweets to extract from the command line
	"""
	try:
		#Get the username and number of tweets from command line
		parser = argparse.ArgumentParser(description='Pass the username and the number of tweets')
		parser.add_argument('--username',nargs='?')
		parser.add_argument('--number_of_tweets',type=int)

		args = parser.parse_args()
		userName = args.username
		noOfTweets = args.number_of_tweets

		getTweets(userName,noOfTweets)

	except Exception as ex:
		print("An error occurred: " + str(ex))
		# creating/opening a file
		f = open("Log.txt", "a")
		# writing in the file
		f.write(str(ex))
		# closing the file
		f.close()
	