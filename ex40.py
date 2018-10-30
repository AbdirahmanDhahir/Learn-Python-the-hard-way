class Song(object):

	def	__init__(self, lyrics):
		self.lyrics = lyrics
		
	def	sing_me_a_song(self):
		for line in self.lyrics:
			print line
		
happy_bday = Song(["Happy birthday to you",
                   "He doesnt want to sue",
				   "So he stopped the song"])
				   
bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()