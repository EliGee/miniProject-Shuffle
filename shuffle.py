#tiny beginner py project to immitate how i imagine a shuffle feature on a playlist works	

import random
import time 

trackList = ["Warra Boga", "Crying [EXPLICIT]", "Get Up", "Get Down", "Get Perpendicular", "Love Girl", "Ramblin Jamblin' Cowboy", "Dopamine Explosion", "H O W L I N G * B L O O D * S K U L L", "BLOGGENKRAUM", "Hype Train", "Party Down the Party City", "My Eyes Shine Fondly on the Unassuming Forests", "Amazing Babe", "Guitar Wizard of Weed Mountain", "Lonely with My Feelings", "Techno Heatdeathoftheuniverse", "En Situ", "My Man Done Done Me Wrong", "My Woman Done Done Me Wrong", "My Nonbinary Genderqueer Person Done Done Me Wrong", "Youth Screaming", "Capitalism is Bad But Yelling is Cool", "Feelings Sword", "YON DUNGEON MAN -- FINAL TEMPTATION LXIX OST", "Elida"]
#OR make a copy of the list called 'unplayed' in the function. 
#select random item on list 
	#hmm, below only works if i DONT PUT SPACES between - and len(songList)
	#if I do, it produces a blank line

def playTrack(song):
	print(f'Now playing \'{song}\'...!\n')
	time.sleep(2)
 
def pickSong(thePlaylist):  
	unheardList = thePlaylist
	#it'll need to be a while loop
	while len(unheardList)>0:
	#hmm, below only works if i DONT PUT SPACES between - and len(songList)
	#if I do, it produces a blank line
		choiceIndex = random.randint(0, len(unheardList)-1)
		songChoice = unheardList[choiceIndex] 
		playTrack(songChoice)
		del unheardList[choiceIndex]
	print("That's all the songs on your playlist!")
pickSong(trackList)

#On a real shuffle, once you played all the songs on the list, it would reset and start the random 
#song selection over with a full list, until the user pressed quit.