print "You enter a dark room with two doors. Do you choice door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There is a gaint bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear kills us, you loos!"
	elif bear == "2":
		print "The bear only eats your legs. good job!"
	else:
		print "Well, doing %s is probably better. Bear run away." % bear
		
elif door == "2":
		print "You stare into the endless abyss at cthulhu's retina."
		print "1. Blueberries."
		print "2. Yellow jacket clothespins."
		print "3. Understanding revovlers yelling melodies."
		
		insanity = raw_input("> ")
		
		if insanity == "1" or insanity == "2":
			print "Your body survives powered by mind of jello. Good job!"
		else:
			print "The insanity rots your eyes into a pool of muck. bad job!"
			
else:
		print "You stumble around and fall on a knife and die. You died!"
