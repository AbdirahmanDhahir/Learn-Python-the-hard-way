the_count = [1, 2, 3, 4, 5]
fruit = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this frist kind of for-loop goes through a lsit
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruit:
	print "A fruit of type: %s" % fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we dont know whats in it 
for i in change:
	print "I got %r" % i 
	
#we can also build lists, first start with an empty one
elements = []

#then use the rang function  to do 0 to 5 count 
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a funcation that lists understand
	elements.append(i)
	
#now we can print them out too 
for i in elements:
	print "Element was: %d" % i 
