#Name: Allison Sharpe
#Date: 09/28/2015
#Assignment: Madlib

#My story line will be based off of the game, Far cry 3 

#Function 1
def begin():

	print "Welcome, my fellow American! You have been kidnapped by Vaas and his pirates and are now stranded on a disclosed island with nothing but your survival instincts to rely on. Every choice you make will have consequences so choose wisely." 
	name = raw_input("Enter your first and last name:") #enter the first and last name of your character
	location = raw_input("Enter a name for your island:") #this is the island where your character will be stranded
	print "Welcome to" + location + "," + name + '.' 
	state = raw_input("What state were you born in?:") #the state you were born in 
	lob = raw_input("What city were you born in?:") #the city you were born in
	dob = raw_input("Enter your date of birth:") #your date of birth
	print "Upon doing research, it seems that you were born in" + lob + "," + state + "," + dob + '.'
	hobby = raw_input("What's your favorite hobby?:") #this will identify your personal past time
 	print "It seems that you part-take in numerous past times, but your fascination with" + hobby + " is off the charts."
 	num_of_days = raw_input("List a number from 50-100:") #the number of days you have to rescue your friends


 	#Array 
 	friends = ["Liza", "Daisy", "Keith", "Oliver", "Riley", "Grant"] #list of friends who are also trapped on the island
 	print "Your friends " + str(friends) + " are also stranded on this island. You will have appoximately" + num_of_days + " days to rescue your friends."
 	
 	tribe = raw_input("What is the name of the tribe that will assist you on this journey?:") #this is the tribe that is well known and is considered "historical" to the village people


	#Dictionary
	dict = {'Name': 'Citra', 'Age': 26, 'Rank': 'Queen of the Rakyat Tribe.'};
 	print "You may believe you are the only one on this journey, but fortunately you are not. There is a tribe called the" + tribe + " tribe. They have a leader who will train you to become a powerful warrior. Here is what you need to know about her: Name: " + dict['Name'] + " Age: " + str(dict['Age']) + " Rank: " + dict['Rank'] 
 
 
 	print "It's now time for you to prepare in making your first purchase. In order to survive you will need the proper equiptment. You will need at least $50 in order to make a purchase and you will need to have $10 left over for savings." 
 	money = raw_input("How much money do you have on you at the moment?:") #the amount of cash you have in order to make purchases
 	print "To help you with your purchases, I am willing to offer you an amount of cash of your choosing."
 	extra_money = raw_input("How much money would you like for me to give you?")
 	
 
#Function 2 	
def total(x, y): 
    totalAmount = int(money) - int(extra_money) #Math operator one
    return totalAmount
total(money, extra_money)


#Conditional Statement 1
if totalAmount > 50: 
	print "You have enough money to make a purchase."
else: 
	print "You cannot purchase any weapons at this time."	
	
		
	print "Great. Now it's time to make a purchase. Use the cash that I gave you to make this purchase. Be careful not to exceed your budget. Remember, you should have at least $10 left over for safe keeping." 
	cost = raw_input("List an estimated price for each weapon:") #this is an estimated price for each weapon
	left = raw_input("How much money will you have left after this transasction?") #this is the amount of money you will have left over


#Function 3	
def total2(x, y):
	totalAmount2 = int(extra_money) - int(cost) #Math operator two
	return totalAmount2
total2(extra_money, cost)
	
	
#Conditional Statement 2	
if money > cost and left >= 10: 
	print "Thank you for your purchase. You may now proceed."
else:
	print "Sorry, you have insufficient funds."	
    
 
#For Loop
print "Well," + name + " It looks like that my work here is done. You now have what it takes to survive the jungle on your own. Countdown in.."
for i in reversed(xrange(11)): #for loop used for countdown
    print i
    
begin()	