from bootup import *
from keep_alive import *

import time
keep_alive()
f = open('data.json','r')
lyrics = data['lyrics']
seen = data['seenLyrics']
count = data['currentCount']
f.close()

  
def generateTweet(lyrics,seen,currentCount):
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
      generateTweet(lyrics,seen,currentCount)
   
    



    
while True:

  generateTweet(lyrics,seen,currentCount)
  time.sleep(10800)
    
    
    
    
  




