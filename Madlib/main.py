#Name: Allison Sharpe
#Date: 09/28/2015
#Assignment: Madlib

def begin():
	#My story line will be based off of the game, Far cry 3 
	print "Welcome, my fellow American! You have been kidnapped by Vaas and his pirates and are now stranded on a disclosed island with nothing but your survival instincts to rely on. Every choice you make will have consequences so choose wisely." 

	#Variables 	
	name = raw_input("Enter your first and last name:") #your first and last name will help to identify who you are
	dob = raw_input("Enter your date of birth:") #your date of birth is required for this process
	lob = raw_input("What city were you born in?:") #your birth residence is also necessary for this process
	location = raw_input("What is the name of the island that you are stranded on?:") #this is the located that you happen to be stranded on at the moment
	tribe = raw_input("What is the name of the tribe that is well known around this island?:") #this is the tribe that is well known and is considered "historical" to the village people
	hobby = raw_input("What's your favorite hobby?:") #this will identify your personal past time
	num_of_days = raw_input("List a number from 50-100:") #the number of days you have to rescue your friends
	money = raw_input("How much money do you have on you at the moment?:") #the amount of cash you have in order to make purchases
	quantity = raw_input("How many weapons would you like to buy?:") #the total amount of weapons available to you for purchase
	cost = raw_input("List an estimated price for each weapon:") #this is an estimated price for each weapon
	amount = raw_input("List your total dollar amount?") #this is the total amount you will spend when purchasing your weapons
	town_name = raw_input("List a town used for buying items:") #this is the town you will go to in order to purchase your weapons


	#Array    
	friends = ["Liza", "Daisy", "Keith", "Oliver", "Riley", "Grant"] #list of friends who are also trapped on the island


	#Dictionary
	dict = {'Name': 'Citra', 'Age': 26, 'Rank': 'Queen of the Rakyat Tribe.'};


	#Function
	def total(quantity, cost):
    	total_cost = cost * amount
    	return total_cost
        
    
	#Conditional Statement 1

	if total(int(cost), int(quantity)) > int(amount):
		result = "You may proceed with your purchases." 
	else:
		result = "You cannot purchase weapons at this time."
	    
    
	#Conditional Statement 2
	#budget = 90

	#if budget > 100:
		#brand = "nike"
	#else:
   	 	#if nothing for else/elif, type "pass" and there will be no errors       


	#For Loop
	#for i in reversed(xrange(11)): #loop used for countdown
    	#i = i+1
    

	#The journey starts here  
	print "Welcome to" + location + "," + name + "." + " Upon doing research, it states here that you were born in" + lob + "," + str(dob) + "." + " It seems that you partake in many past time hobbies, but you seem to be very intrigued with" + hobby + "." + " Your friends" + str(friends) + " are also trapped here on this island and are being held captive by Vaas and his pirates. You will have an approximately" + str(num_of_days) + " days to rescue your friends before they are sold into slavery. Don't worry, though. You're not alone. You have the" + tribe + " tribe to assist you on your journey. It seems that they have a leader. Here is her information:" + " Name: " + dict['Name'] + " Age: " + str(dict['Age']) + " Rank: " + dict['Rank'] + " In order to survive these parts, you will need to purchase at least " + str(quantity) + " weapons. Each weapon costs " + cost + "." 
	
	