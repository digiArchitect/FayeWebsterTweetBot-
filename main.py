from bootup import *
from keep_alive import *

import time
keep_alive()

f.close()

  
def generateTweet():
  f = open('data.json','r')
  data = json.load(f)
  lyrics = data['lyrics']
  seen = data['seenLyrics']
  if(len(lyrics) > 0):
    s = lyrics[0]
    if(s not in seenLyrics):
      client.create_tweet(text=s)
      seen.append(s)
      lyrics.pop(0)
      dictionary = {
      'currentCount': data['currentCount'],
      'lyrics': lyrics,
      'seenLyrics': seen
         
    }
    changeData(dictionary)
      
      
  else:
    lyrics.pop(0)
    generateTweet()
   
    



    
while True:
  generateTweet()
  keep_alive()
  time.sleep(1800)
    
    
    
    
  




