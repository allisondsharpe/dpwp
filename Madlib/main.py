#Name: Allison Sharpe
#Date: 09/28/2015
#Assignment: Madlib


#Strings 
name = raw_input("Enter your name:") #enters name of user
activity = raw_input("Enter an activity:") #enters an activity
animal = raw_input("Enter an animal:") #enters an animal


#Numbers 
birthdate = raw_input("Enter your birthdate:") #enters user's birthdate
age = raw_input("Enter your age:") #enters age
year = raw_input("Enter the current year:") #enters current year
number = raw_input("List a number from 1-2:") #enters a number from 1-2


#Story
print "Hello," + name + " and welcome to my Madlib! It says here that you were born" + birthdate + " and that you are currently" + age + " years old. It is now" + year + " and you want nothing more than to go spend your day at the town. Let's begin our journey, shall we?" 


#Conditional Statement 1  
if age > 18 and age < 80: #logical operator
	print name + " will go to the store without guidance." 
else:
	print name + " will need a parent/care-taker in order to go to the store."	


#Story(Cont.)
print name + " went to the store to purchase some candy." " Each piece costs $5."	
	
		
#Function 1
def total(a, b): #my two parameters
    candy = a + b #Math Operator
    return candy #returns function

x = total(5, 5);
print "$" + str(x) + " is your total amount."		


#Conditional Statement 2
if number == "1":
	print "Let's go to the zoo!"
if number == "2":
	print "Let's go to the zoo!"
else: 
	pass			


#Story(Cont.)
print "So," + name + " have you ever been to the zoo before? You said your favorite animal was a" + animal + ". The zoo probably has them here. Let's go buy a drink and a snack first. A drink costs $5 and a snack costs $6."


#Function 2
def total(a, b): #my two parameters
    snack_beverage = a + b #Math Operator
    return snack_beverage #returns function

x = total(5, 6);
print "$" + str(x) + " is your total amount."	
   
   
#Story(Cont.)    
print "Whew. That was fun. Now let's go back home. You said your favorite activity was" + activity + ". That does sound like fun, but let's do that another time."
    
    
#Array
actors = ["Johnny Depp", "Heath Ledger", "Ann Hathaway", "James Franco"]
print "How about now we watch some movies? Particularly ones that involve " + str(actors)


#Dictionary
dict = {"Farcry 3": "Vaas Montenegro"} 
print "Now it's time to play some video games. My favorite game and character is " + str(dict)

 
#For Loop
print "Well," + name + ", Thank you for your time. Now let's countdown.."
for i in reversed(xrange(11)): #for loop reversed for countdown
    print i       
