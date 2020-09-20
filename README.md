# miniProject-Shuffle

Tiny beginner python project where I emulate how I imagine a shuffle feature on a media player might be coded. 

Important info I learned from this project: 

while len(unheardList)>0:
	#hmm, below only works if i DONT PUT SPACES between - and len(songList)
	#if I do, it produces a blank line
		choiceIndex = random.randint(0, len(unheardList)-1)
		songChoice = unheardList[choiceIndex] 
