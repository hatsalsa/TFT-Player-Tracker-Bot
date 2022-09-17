from schedule import every, repeat, run_pending
import os
import tweepy
import time
from dotenv import load_dotenv
import requests
import datetime
from halo import Halo


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
   print('\033[1;92m' + '✔ Tweeted successfully' + '\033[0m', end="\r")
 elif division == "DIAMOND":
  api.update_status_with_media(f'SHE FINALLY DID IT !!! - {division}-{div_rank} WITH {lp}LP IT ONLY TOOK HER  {str(int(wins))} WINS.', "letsgo.gif")
  print("SHE FINALLY REACHED DIAMOND")
  exit()


# define the countdown func.
# @Halo(text='', spinner='dots')
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:d}:{:02d}:{:02d}'.format(hours, mins, secs)
        # print('\033[1;33m' + 'Tweeting in ' + timer + '\033[0m', end='\r')
        time.sleep(1)
        t -= 1

# spinner = Halo(text='\033[1;33m' + 'Timer is running' + '\033[0m', spinner='dots')
# function call
os.system('cls||clear')
print('\033[1;91m' + 'Starting job...' + '\033[0m')

@repeat(every(1).seconds)
def main():
  # print('\033[1;32m' + 'Running timer now...' + '\033[0m')
  spinner = Halo(text='\033[1;33m'+'Waiting for cooldown.' + '\033[0m', spinner='dots', color='green')
  spinner.start()
  countdown(100)
  spinner.succeed(text='\n\033[1;34m' + 'Now we send the tweet!' + '\033[0m')
  spinner.stop()
  # print('\n\033[1;34m' + 'Sending tweet...' + '\033[0m')
  # os.system('cls||clear')
  check_rank()
  print('\n\033[1;37m'  + 'Restarting Job...' + '\033[0m')
while True:
    try:
      run_pending()
      time.sleep(1)
    except tweepy.TweepError as error :
      raise error
      exit()

if __name__ == "__main__":
 main()
