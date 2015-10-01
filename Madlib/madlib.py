#Name: Allison Sharpe
#Date: 09/28/2015
#Assignment: Madlib

#My story line will be based off of the game, Far cry 3 
print "Welcome, my fellow American! You have been kidnapped by Vaas and his pirates and are now under surveillance. Every decision you make will have a purpose so choose wisely." 

#Variables 	
name = raw_input("Enter your first and last name") #your first and last name will help to identify who you are
dob = raw_input("Enter your date of birth") #your date of birth is required for this process
lob = raw_input("Where were you born?") #your birth residence is also necessary for this process
location = raw_input("Where are you stranded now?") #this is the located that you happen to be stranded on at the moment
hobby = raw_input("What's your favorite hobby?") #this will identify your personal past time
numOfDays = raw_input("List a number from 50-100.") #the number of days you have to rescue your friends
amount = raw_input("How many weapons would you like to buy?") #the total amount of weapons available to you for purchase
cost = raw_input("List an estimated price for each weapon.") #this is an estimated price for each weapon
townName = raw_input("List a town used for buying items.") #this is the town you will go to in order to purchase your weapons


#Array    
friends = ["Liza", "Daisy", "Keith", "Oliver", "Riley", "Grant"] #Your list of friends who are also trapped on the island
friends.append("Dr. Earnhardt") #Dr. Earnhardt is added to this list later in the series


#Function
def totalAmount(amount, cost):
    total = cost * amount
    return total


#Dictionary
#dict = dict() 
#dict = {1:'',2:'',3:'',4:'',5:''}
#type = int(something)
#list = someName[type]


#While Loop
#i = 0
#while i<9: #countdown to when journey begins
    #i = i+1
    
    
#Conditional Statement 1
#budget = 90

#if budget > 100:
	#brand = "nike"
#else:
    #if nothing for else/elif, type "pass" and there will be no errors    
    
    
#Conditional Statement 2
#budget = 90

#if budget > 100:
	#brand = "nike"
#else:
    #if nothing for else/elif, type "pass" and there will be no errors        


#The journey starts here 
print "Welcome to " + location + ",", name + ". " + "Upon doing research, it states here that you were born in " + lob + "," + str(dob) + ". " + "It seems that you partake in many past time hobbies, but you seem to be very intrigued with " + hobby + ". " + "Your friends " + str(friends) + "are also trapped here on this island and are being held captive. You will have an approximately " + str(numOfDays) + " days to rescue your friends before they are sold into slavery. I would recommend going to " + townName + " and purchasing appoximately " + str(amount) + " weapons. By purchasing this amount of weapon(s), the total cost will be " + total 