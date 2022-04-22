import os
import tweepy
import json
from lyricsgenius import Genius
from helper import *
import re
import unidecode
bearer = os.environ['BEARER']
secret = os.environ['Consumer Secret']
acc = os.environ['Access Key']
acc_secret = os.environ['ACCESS SECRET']
key = os.environ['Consumer Key']
token = os.environ['gtoken']
genius = Genius(token)
f = open('data.json','r')
file1 = open("MyFile.txt","a")
data = json.load(f)
currentCount = data["currentCount"]
seenLyrics = data["seenLyrics"]
f.close()








#print(json.dumps(genius.album_tracks(id), indent=4, sort_keys=True))
client = tweepy.Client(consumer_key=key,
                       consumer_secret=secret,
                       access_token=acc,
                       access_token_secret=acc_secret) 

##updates an album

#sets the current album

#generates the tracks from an album
#def tracks(id):
 # tracks = genius.album_tracks(894704)
  #tracks = tracks['tracks']
  #albumCount = len(tracks)
  #print(json.dumps(tracks, indent=4, sort_keys=True))
  #for x in tracks:
   # print(json.dumps(x, indent=4, sort_keys=True))
    #Weird error where if there is an item in the"()" it produces incorrect song so have to split
    #s = x['song']['title'].split("(",1)[0]
   # trackIds.append(s)
 # print(trackIds)
#def genLyrics(name):
  
  
 

  

def updateLyrics():
  all_lyrics = json.dumps(genius.search_artist("Faye Webster").save_lyrics(extension="txt"))
  

#with open("data.json", "w") as outfile:
    #outfile.write(all_lyrics)
#print(genius.search_song(trackIds[0],"Faye Webster").lyrics)
      #.lyrics)
                        #).lyrics)

# Establish a connection to the Database and create
# a connection object



    

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
    updateLyrics()
    
  

#reads the lyrics in a file
def readLyrics():
        fileObj = open("lyrics.txt", "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return cleanupLyrics(words)
#cleans up the lyrics
def cleanupLyrics(lyrics):
  newLyrics = []
  for x in lyrics:
    #Figure out the weird unicode error
    x = unidecode.unidecode(x)
    badStrings = ["Verse","Chorus","String","Outro","Embed","Bridge","Lyrics"]
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
  checkNew()
  dictionary = {
  "currentCount": currentCount,
  "lyrics" : readLyrics(),
  "seenLyrics": seenLyrics
}
  print("hey im running")
  with open("data.json", "w") as outfile:
    json.dump(dictionary, outfile)
  
print(readLyrics())
#commitLyrics()

 # print(x['id'])
#print(totalTracks)
#print(len(genius.album_tracks(894704)))
#print(json.dumps(genius.artist_songs(1126994), indent=4, sort_keys=True))
#print(json.dumps(tracks, indent=4, sort_keys=True))






#set()
#if (currentAlbum == ''):
  #arr = list(albumIters.keys())
  #currentAlbum = arr[0]