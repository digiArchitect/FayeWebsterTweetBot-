import os
import tweepy
from lyricsgenius import Genius
from helper import *
import unidecode
bearer = os.environ['BEARER']
secret = os.environ['Consumer Secret']
acc = os.environ['Access Key']
acc_secret = os.environ['ACCESS SECRET']
key = os.environ['Consumer Key']
token = os.environ['gtoken']
genius = Genius(token)
f = open('data.json','r')
data = json.load(f)
currentCount = data["currentCount"]
seenLyrics = data["seenLyrics"]
f.close()








#print(json.dumps(genius.album_tracks(id), indent=4, sort_keys=True))
client = tweepy.Client(consumer_key=key,
                       consumer_secret=secret,
                       access_token=acc,
                       access_token_secret=acc_secret) 


  
  
 

  

def updateLyrics():
  all_lyrics = json.dumps(genius.search_artist("Faye Webster").save_lyrics(extension="txt"))
  readLyrics()
  





    

#Checks if there are more lyrics
def checkNew():
  tracks = genius.artist_albums(1126994)
  tracks = tracks["albums"]
  totalTracks = 0
  for x in tracks:
    tracks = genius.album_tracks(x['id'])
  
    tracks = tracks["tracks"]
    totalTracks += len(tracks)
  if(currentCount != totalTracks):
    currentCount == totalTracks
    return updateLyrics()
  return readLyrics()
    
  

#reads the lyrics in a file
def readLyrics():
        fileObj = open("Lyrics_FayeWebster.txt", "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return cleanupLyrics(words)
  
#cleans up the lyrics
def cleanupLyrics(lyrics):
  newLyrics = []
  for x in lyrics:
    #Figure out the weird unicode error
    x = unidecode.unidecode(x)
    badStrings = ["Verse","Chorus","String","Outro","Embed","Bridge","Lyrics","Instrumental break","Faye Webster"]
    for bad in badStrings:
      if bad in x:
        x = x.replace(bad, "")
    x = ''.join([i for i in x if not i.isdigit()])

    invalid = ["[", "]"]
    x = ''.join([i for i in x if not i in invalid])
    x = x.strip().lower()

      
    
      

    newLyrics.append(x)

  newLyrics = [i for i in newLyrics if i]
  return newLyrics
def commitLyrics():
  lyrics = checkNew()
  dictionary = {
  "currentCount": currentCount,
  "lyrics" : lyrics,
  "seenLyrics": seenLyrics
  }
  changeData(dictionary)
  
commitLyrics()

