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
if age > 18 or age < 80:
	print name + " will go to the store without guidance." 
else:
	print name + " will need a parent/care-taker in order to go to the store."	



