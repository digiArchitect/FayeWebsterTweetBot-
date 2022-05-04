from bootup import *
from keep_alive import *

import time
keep_alive()
commitLyrics()
f = open('data.json','r')
lyrics = data['lyrics']
count = data['currentCount']
f.close()

#Tweets lyric and then updates it   
def getLyric(lyrics):
  s = lyrics.pop(0)
  client.create_tweet(text=s)
  dictionary = {
    'currentCount': count,
    'lyrics': lyrics,
       
  }
  changeData(dictionary)
  return lyrics

   
    



    
while True:
 lyrics = getLyric(lyrics)
 time.sleep(10800)
    
    
    
    
  




