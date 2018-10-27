from sys import exit 

def hero_return():
	print "You defeated the dragon and you returned home."
	print "You are welcomed home like a hero by the king."
	print "The king offers you 1,000 gold or a wife."
	print " gold or wife?"
	
	next = raw_input("> ")
	
	if "gold" in next:
		print "You become flithy rich and live become respected noble"
		exit(0)
	elif "wife" in next:
		print "You live happliy ever after and have nice family life."
		exit(0)
	else:
		dead("Please enter a vaild option")
		
def return_home():
	print "You fail you misson"
	print "You returned home without defeating the dragon"
	print "You are shamed by the king and loss you knight hood."
	print "Do you go back to the cave or be dishonured?"
	print "back or shame?"
	
	next = raw_input("> ")
	
	if next == "back":
		start()
	elif next == "shame":
		return_home()
	else:
		dead("please enter a vaild option")
		
		
def dragon():
	print "You have entered the dragon's cave"
	print "There is a dragon in front if you."
	print "you have three options to defeat the dragon."
	print " 1. attack 2. defened 3. dodge"
	print "you can use the option togther to defeat the dragon."
	print "How do you defeat th dragon?"
	dragon_attack = False
	
	while True:
		next = raw_input("> ")
		
		if next == "dodge":
			print("The dragon looks at you and eats you alive")
		elif next == "defend" and not dragon_attack: 
			print("You didnt attack and you become the dragons lunch")
			dragon_attack = True
		elif next == "attack" and dragon_attack:
			print ("The dragon is defeated and you are a hero")
			hero_return()
		else:
			print "Please enter your options correctly."
			

def dead(why):
	print why, "you died"
	exit(0)
	
	
def start():
	print "In front of you is a dragon cave."
	print "You enter the dragon cave at your own risk."
	print "It's dark"
	print "Do you light a toruch or not?"
	print "yes or no?"
	
	next = raw_input("> ")
	
	if "yes" in next:
		dragon()
	elif "no" in next:
		return_home()
		
start()
		

	


	
