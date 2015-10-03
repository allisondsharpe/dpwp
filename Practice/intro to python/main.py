#----BASIC----

#one lined comments
'''
Multiple lined comments/Doc strings
'''

#use underscores in place of camelCase
first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your name") #don't use semicolons at end
#print "Hello there, ", response

birth_year = 1965
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old"

#str(age) = converts number into string
#int(age) = converts string into number



#----IF/ELSE/ELIF----

#in python, use colon ':' in order to declare if/else statements instead of curly braces
budget = 90

if budget > 100:
    brand = "nike"
    print "Yay! we can buy cool " + brand + " shoes!"
elif budget > 70: #elif (else/if)
    print "We can at least get some generic sneakers"
else:
    print "No cool shoes for me."
    #if nothing for else/elif, type "pass" and there will be no errors



#----ARRAYS----

characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi won") #add characters to array
print characters
#print characters[0] #print characters by index number

movies = dict() #create dictionary object
movies = {"Star Wars": "Darth Vader", "Silence of the Lambs":"Hannibal Lecter"} #key is before colon and value of key is after colon, ex: "Star Wars":"Darth Vader"
print movies["Star Wars"]



#----LOOPS----

'''
#While loop
i = 0
while i<9: #use colon after declaring while or for loop
    print "The count is", i
    i = i+1

#For loop
for i in range(0,10): #count will only go to 9 because it stops at 10
    print "The count is", i
    i = i+1

#For each loop
rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    print r #prints out list
    print "One of the best rappers is " + r #prints out list with string infront of each item
'''



#-----FUNCTIONS------



#EXAMPLE 1

x = 2 #global variables will be above the function(s)

def calcArea(h, w): #create function with parameters
    area = h * w
    return area + x

a = calcArea(20, 40); #call function/invoke
#print "My area is " + str(a) + "sqft" #add "str" to variable a to print string
#print a



#EXAMPLE 2

'''
weight = 200
height = 63
message = '''
#Your height is {height} and your weight is {weight}
'''
message = message.format(**locals())
print message
'''



#EXAMPLE 3 (HTML)

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>

<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
#get body and title value

message = message.format(**locals())
print message


