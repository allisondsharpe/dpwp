#Name: Allison Sharpe
#Date: 09/28/2015
#Assignment: Madlib

#My Madlib is a random story I created involving multiple events during a day out


#Strings 
name = raw_input("Enter your name:") #Enters name of user
activity = raw_input("Enter an activity:") #Enters an activity
animal = raw_input("Enter an animal:") #Enters an animal


#Numbers 
birthdate = raw_input("Enter your birthdate:") #Enters user's birthdate
age = raw_input("Enter your age:") #Enters age
year = raw_input("Enter the current year:") #Enters current year
number = raw_input("List a number from 1-2:") #Enters a number from 1-2


#Story(Beginning)
print "Narrator: Hello, " + name + " and welcome to my Madlib! It says here that you were born in " + birthdate + " and that you are currently " + age + " years old. It is now " + year + " and you want nothing more than to go spend your day at the town. Let's begin our journey, shall we? First we should stop by the store and purchase some yummy candy." 


#Conditional Statement 1  
if age > "18" and age < "80": #logical operator
	print name + " will go to the store without guidance." 
else:
	print name + " will need a parent/care-taker in order to go to the store."	


#Story(Cont.)
print name + " went to the store to purchase some candy." " Each piece costs exactly $5."	
	
		
#Function 1
def total(a, b): #My two parameters
    candy = a + b #Math Operator
    return candy #Returns function

x = total(5, 5);
print "$" + str(x) + " is your total amount all together."		


#Conditional Statement 2
if number == "1": #If user enters the number "1"
	print "Narrator: The zoo sounds like fun. Let's go!"
if number == "2": #If user enters the number "2" 
	print "Narrator: The zoo sounds like fun. Let's go!"
else: 
	print "Narrator: Goodbye." #User will receive a "goodbye" message if entered any other number except 1 or 2			


#Story(Cont.)
print "Narrator: So, " + name + " have you ever been to the zoo before? You said your favorite animal was a " + animal + ". The zoo probably has them here. Let's go buy a drink and a snack first. A drink costs $5 and a snack costs $6."


#Function 2
def total(a, b): #My two parameters
    snack_beverage = a + b #Math Operator
    return snack_beverage #Returns function

x = total(5, 6);
print "$" + str(x) + " is your total amount all together."	
   
   
#Story(Cont.)    
print "Narrator: Whew. That was fun. Now let's go back home. You said your favorite activity was " + activity + ". That does sound like fun, but let's do that another time."
    
    
#Array
actors = ["Johnny Depp", "Heath Ledger", "Ann Hathaway", "James Franco"]
print "Narrator: How about now we watch some movies? Particularly ones that involve " + str(actors) + '.'


#Dictionary
dict = {"Farcry 3": "Vaas Montenegro"} 
print "Narrator: Now it's time to play some video games. My favorite video game and character is " + str(dict) + '.'

 
#For Loop
print "Narrator: Well, " + name + ", Today was a fun day. Now let's countdown to midnight.."
for i in reversed(xrange(11)): #for loop reversed for countdown
    print i       
