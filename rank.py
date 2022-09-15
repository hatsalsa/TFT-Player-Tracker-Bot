import os
import sys
import tweepy
import schedule
import time
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('RIOT_API_KEY')
api_uri = os.getenv('RIOT_API_URI')
consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET_KEY')
bot_key = os.getenv('TWITTER_BOT_TOKEN')
bot_secret = os.getenv('TWITTER_BOT_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(bot_key, bot_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)



def check_rank():
 # concat the API ENV keys.
 api_url =  api_uri + "?api_key=" + api_key
 # send the request to RIOT GAMES API.
 resp = requests.get(api_url)
 # parse the response to JSON format.
 player_info = resp.json()
 # Add the rank tier  to the variable rank
 rank = player_info[0]['tier']
 #  If the rank is PLATINUM send the first message if it's DIAMOND send the second message and end the program.
 if rank == 'PLATINUM':
   api.update_status("NOT YET, SHE IS " + player_info[0]['tier'] + "-" + player_info[0]['rank'])
   print("TWEET POST IT")
 elif rank == "DIAMOND":
  api.update_status_with_media("SHE FINALLY DID IT !!! - " + player_info[0]['tier'] + "-" + player_info[0]['rank'], "letsgo.gif")
  print("SHE FINALLY REACHED DIAMOND")
  sys.exit()


def main():
 # Run the tweet service every day at 8:30 AM
 schedule.every().day.at("08:30").do(check_rank)
while True:
    try:
     schedule.run_pending()
     time.sleep(1)
    except  tweepy.TweepError as e:
     raise e

if __name__ == "__main__":
 main()