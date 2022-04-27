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
  for x in lyrics:
    if(x not in seen):
      time.sleep(10800)
      client.create_tweet(text=x)
      seen.append(x)
      dictionary = {
      'currentCount': data['currentCount'],
      'lyrics': lyrics,
      'seenLyrics': seen
       
    }
      changeData(dictionary)


   
    

generateTweet(lyrics,seen,currentCount)

    

    
    
    
    
  




