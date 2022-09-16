from itertools import count
from schedule import every, repeat, run_pending
import os
import sys
import tweepy
import schedule
import time
from dotenv import load_dotenv
import requests
import datetime
x = datetime.datetime.now()
load_dotenv()

api_key = os.getenv('RIOT_API_KEY')
api_uri = os.getenv('RIOT_API_URI')
consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET_KEY')
bot_key = os.getenv('TWITTER_BOT_TOKEN')
bot_secret = os.getenv('TWITTER_BOT_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(bot_key, bot_secret)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=bot_key,
    access_token_secret=bot_secret,
)
api = tweepy.API(auth, wait_on_rate_limit=True)



def check_rank():
 # concat the API ENV keys.
 api_url =  api_uri + "?api_key=" + api_key
 # send the request to RIOT GAMES API.
 resp = requests.get(api_url)
 # parse the response to JSON format.
 player_info = resp.json()
 # Add the rank tier  to the variable rank
 division = player_info[0]['tier']
 div_rank = player_info[0]['rank']
 lp = player_info[0]['leaguePoints']
 wins = player_info[0]['wins']
 losses = player_info[0]['losses']
 #  If the rank is PLATINUM send the first message if it's DIAMOND send the second message and end the program.
 if division == 'PLATINUM':
   client.create_tweet(text=f'NO, AS OF {x.strftime("%c")} SHE IS {division}-{div_rank} WITH {str(int(lp))}LP AND {str(int(losses))} LOSSES https://www.twitch.tv/yoonahkorn')
   print("\nTWEET POST IT", end="\r")
 elif division == "DIAMOND":
  api.update_status_with_media(f'SHE FINALLY DID IT !!! - {division}-{div_rank} WITH {lp}LP IT ONLY TOOK HER  {str(int(wins))} WINS.', "letsgo.gif")
  print("SHE FINALLY REACHED DIAMOND")
  exit()


# define the countdown func.
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print("Tweeting in " + timer, end="\r")
        time.sleep(1)
        t -= 1

# function call
print("Starting job...")
@repeat(every(10).seconds)
def main():
  print("Running timer now...", end="\r")
  countdown(10800)
  print("\nSending tweet...", end="\r")
  # os.system('cls||clear')
  check_rank()
  print("\nRestarting Job...", end="\r")
while True:
    try:
      run_pending()
      time.sleep(1)
    except:
     exit()

if __name__ == "__main__":
 main()