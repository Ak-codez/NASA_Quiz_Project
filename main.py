# VARIABLES
# String variables
# name = "Akshith"
# favfood = "pizza"
# email="lord.kothi@gmail.com"
#
# printing string and variable at the same time: use f-string, "f", and use curly brackets for your var
#
# print(f"Hello, {name}")
# print(f"You like {favfood}")
# print(f"Your mail is {email}")
#
#
# Integer variables
# age = 14
# tomato = 10
#
# Integer variables have no quotes
# Only have whole numbers; no decimals
#
# print(f"You are {age} years old")
# print(f"You are buying {tomato} tomatoes")
#
#
# Float variable
# height=172.23
# price= 25.10
#
# Floats contain decimals
#
# print(f"You are {height} centimeters tall")
# print(f"The price of {tomato} tomatoes is {price} rupees")
#
#
# Boolean variable
# Fact = True
# Lie = False
#
# Either true or false
# T and F of the true and false are always capital according to syntax rules
#
# print(f"The Sun revolves around the Earth: {Lie}")
# print(f"The Earth revolves around the Sun: {Fact}")
#
# Is mostly used in if-else statements
# is_animal = True
# if is_animal:
#     print("That is an animal")
# else:
#     print("That isn't an animal")
#
# ##########################################################
#
# TYPE CASTING
# Converting a variable from one type, i.e. string, integer, float, or boolean, to another type
# syntax:
#     str()
#     int()
#     float()
#     bool()
# first_name = "Ak"
# current_age = 14
# current_height = 172.72
# is_student = True
#
# Use the type() function and input the variable to identify the type, thereby print
#
# print(type(first_name))
# Output; <class 'str'>
# print(type(is_student))
# Output; <class 'bool'>
#
# Converting one type to another:
# current_height=int(current_height)
# print(current_height)
# Output is rounded to nearest whole number
#
# If a string is typecast into a boolean:
#     Regardless of what the string is, the output is True
#     If the string is left empty, then the output is False--> can be useful in online forms where if a name is not entered then the user is reprompted due to a False output
#
# ###########################################################
# Input
# use input() function
#
# name= input("Input your name:")
#
# print("Your name is",name)
# print(f"Your name is {name}")
#
# All inputs for the input function are stored as a string
# If you want to perform mathematical operations to your variable, example "age", you can use int(input()) instead of just input
# Similarly, you can use float(input()) or bool((input))
#
# a= int(input("What is your age?:"))
# print(f"You are {a} years old. Next birthday, you will turn {a+1} years old")
#
# ###################################################################################################################################
#
# Arithmetic Operators
# + is used to add different variables
# Augmented Assignment Operators: Can be used when you are referring back to the variable in the operation:
#     x=x+1 can be written as x += 1
#
# items = 1
# items += 1
# print(items)
# Output will be 2
#
# - for subtraction, * for multiplication, / for division, ** for exponentiation, % for modulus (giving an output of a remainder
#
# Built-in functions:
# Round / round() rounds a function to the nearest int
# Absolute / abs() returns the absolute value of a number
# Power / pow(base,exponent) does exponentiation in a single line
# Maximum / max(__,__,...) returns the maximum value of a given list
# Minimum / min(__,__,...) returns the minimum value of a given list
#
# Math module
# import math
# print(math.pi)
# print(math.e)
#
# ##############################################################
# If and Else condition statements
# if and else are for conditions; "if" something, then do something, "else," do another thing
# always have a colon after the statement's condition
#
# age = int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible for a driver's license")
# else:
#     print("You are not eligible for a driver's license")
#
# Elifs can be used to set in-between parameters
# if age>=99:
#     print("You are too old")
# elif age>=18:
#     print("You are eligible for a driver's license")
# elif age<=0:
#     print("Please give a realistic age")
# else:
#     print("You are not eligible for a driver's license")
#
# If you want to use strings as a comparision, use the comparision operator "==" different from the assignment operator "="
# Example:
# name= input("What is your name?:")
# if name=="Akshith":
#     print("You are Akshith")
# elif name=="Michael Jackson":
#     print("You are Michael Jackson")
# elif name=="":
#     print("You didn't type in a name!")
# else:
#     print("You are neither Akshith nor Michael Jackson")
#
# If you have a boolean variable, you can use the variable name itself as a condition
# example:
# for_sale = True
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")
#
# ###############################################################################
#
# Python Calculator practice
# operator = input("Please select an operator: + - * / :")
# num_1= float(input("What is your first number?:"))
# num_2= float(input("What is your second number?:"))
#
# if operator=="+":
#     print("The sum of the two numbers is:", num_1+num_2)
# elif operator=="-":
#     print("The difference of the two numbers is:", num_1 - num_2)
# elif operator=="*":
#     print("The product of the two numbers is:", num_1 * num_2)
# elif operator=="/":
#     print("The quotient of the two numbers is:", num_1 / num_2)
# else:
#     print("Please input an appropriate operator")
#
# ###########################################################################
# Logical Operators
# Can evaluate multiple conditions in the condition statements
# or = If atleast one condition is true, the output is true
# and = Only if both conditions are true, the output is true
# not = If the output is true, it converts it into not True (inverts the condition)
#
# OR
# temp = 25
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The event is cancelled")
# else:
#     print("The event is not cancelled")
#
# AND and NOT combination
# temp = 25
# is_sunny = True
# if temp>=30 and is_sunny:
#     print("It is too hot to go outside. It is sunny")
# elif temp<=18 and is_sunny:
#     print("It is too cold to go outside. It is sunny")
# elif  22 < temp < 28 and is_sunny:
#     print("It is warm and sunny")
# elif temp>=30 and not is_sunny:
#     print("It is too hot to go outside. It is cloudy")
# elif temp<=18 and not is_sunny:
#     print("It is too cold to go outside. It is cloudy")
# elif  22 < temp < 28 and not is_sunny:
#     print("It is warm and cloudy")
#
# ####################################################################
# Conditional expressions
# one line shortcut for if-else statements
# You can assign one of two values based on a condition; return a specific condition if said condition is true else return another result
# Syntax; X if condition else Y
#
# num = int(input("Input a number:"))
# print("Even" if num%2==0 else "Odd")
#
# ######################################################################
# String methods
#
# name= input("Enter your full name:")
#
# 1. Length
# length = len(name)
# print(length)
# The spaces are also considered characters, hence, inputting "Akshith Thokala" will return 15
#
# 2. Finding the first instance of a character in the input
# For this, we have to write the variable followed by a dot then the appropriate thing
# first = name.find("a")  #This "a" is case-sensitive
# print(first)
# When counting the string and finding the first instance of an input character, the computer starts from 0. Thus, if the input is "Akshith" and you want to find the first instance of "s," the result would be "2"
#
# For the last occurence of a charater, however, you have to use var.rfind (the "r" here being reverse)
# last = name.rfind("h")
# print(last)
# Here, if you input Akshith, the last occurence of "h" is position 6
#
# If you try to find something that is not in your find, the output will be "-1"
#
# All of the following do not need arguments in their parentheses, i.e. you can write name.upper() and nothing in parentheses
# .capitalize makes the first character capitalized
# .upper makes all the character upper case
# .lower makes all the character lower case
# .isdigit returns a True or False, checking if the input is a digit or not, doesn't return True with combos of string and int
# .isalpha returns a True or False, checking if the input is using only alphabets
#     keep in mind that a space is not an alphabet
#
#
# Practice
# phone_number = input("Enter your phone number:")
# phome numbers typically have spaces between the digits
# spaces = phone_number.count(" ")
#
#
# You can also replace things
# let's say you wanna replace the spaces in the number with hyphens
# replace = phone_number.replace(" ","-")
#
#
#
# print(spaces)
# print(replace)
#
# ###############
#
# Exercise on string stuff
# Validating user inputs
# 1. Ensure the username is no more than 12 characters
# 2. Ensure the username does not contain spaces
# 3. Ensure the username does not contain digits
#
# username = input("Enter your username:")
#
# if len(username)>12:
#     print("Your username can not be more than 12 characters long")
# elif not username.find(" ")==-1:
#     print("Your username can not contain spaces")
# elif not username.isalpha():
#     print("Your username can only contain alphabets")
# else:
#     print(f"Your username '{username}' is saved")
#
#
#
#
# #####################################################################
# String indexing
# Allows us to access certain elements of a sequence using square brackets, a.k.a indexing operators
# We can access the start, end, and step
#
# Ex:
#
# creditcard_number = "1234-5678-9012-3456"
#
# print(creditcard_number[0])
# The standard syntax in indexing is [start:end:step]
# the first index is always 0, thus we are finding the first element
# If you want to print the first four digits, you use creditcard_number[0:4], you're starting at index 0 and ending at index 4
# print(creditcard_number[0:4])
#
# If you want python to assume you're starting from the beginning of the string, then you can leave the start area empty:
# print(creditcard_number[:4])
# If you want python to assume the print will end till the end of the string, then leave the end area empty
# print(creditcard_number[4:])
#
# If you want to work backwards, use negative numbers
# print(creditcard_number[-5])
# print(creditcard_number[-5:-1])
#
# Step is basically skipping stuff
# print(creditcard_number[::2])
#
# A step of -1 will reverse the print
# print(creditcard_number[::-1])
#
# ##################################################################################
# Format Specifiers
# Used in the context of f-strings
# {value:flag} formats the value based on the flag specified
#
#
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
#
# Rounding a decimal
# We add a colon after the value and choose a flag
# In this case, we use the decimal point "." and then the place we want to round followed by "f" indicating the float value
# print(f"Price 1 is {price1:.2f}")
#
# To allocate spaces, just write the number of spaces you want
# Keep in mind that the string itself also counts in the space
# Therefore, using this can help align the last characters of the strings
# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")
#
# To precede the numbers with zeros, just add a zero upfront
# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")
#
# For alignment, left= <   right= >    center = ^
# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:<10}")
#
# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")
#
# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")
#
# To add a plus before the values, put plus after the colon (If there are negative signs, they will stay). This is useful for showing an increase or decrease in money, say
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")
#
# To add a comma for every 3 digits (like 1,000) add a comma after colon
# price4 = 3129301.332
# print(f"Price 4 is {price4:,}")
#
#
# To mix and match format specifiers, just add them continuously without any separators
# Example:
# print(f"Price 4 is ${price4:>20,.2f}")
# Sometimes errors will come so try to fix the sequence
#
# #########################################################################################################################
# WHILE LOOPSSSSSSSSSSS
# Executing code while some condition remains true
#
# name = input("Enter your name:")
# if name == "":
#     print("The field is blank; please enter your name")
# else:
#     print(f"Hello {name}")
# In this simple code, we can check if the user's name is left blank. But if you want to keep prompting the user to type their name, use a while loop
# while name == "":
#     name= input("You did not enter your name, reenter it here:")
# print(f"Welcome {name}")
#
# another example:
# age = int(input("Input your age:"))
# while not 0 < age < 110:
#     age = int(input("Please input a realistic age:"))
# print(f"You are {age} years old")
#
# ###########################################################################################################################
# Compound interest calc prac
#
# principal = float(input("What is the principal amount?:"))
# rate = float(input("What is the interest rate?:"))
# time = int(input("What is the number of years elapsed?:"))
# Final_amount = principal*(1+rate/100)**time
# print(f"The final amount is ${Final_amount:.2f}")
#
# #################################################################################################
# FOR LOOPSSSSSSSSSSS
# To execute a code for a fixed number of times
#
# To count to 10:
# for x in range(1,11):
#     print(x)
#
# To count backwards:
# for x in reversed(range(0,11)):
#     print(x)
# print("Happy birthday!")
#
# String:
# credit_num = "1234-5678-9012-3456"
# for x in credit_num:
#     print(x)
#
# There are two important keywords you can use in both while and for loops:
# Continue and Break
# For example, if you want to count to 20 but wanna skip 10, you can use continue:
# for x in range(1,21):
#     if x==10:
#         continue
#     else:
#         print(x)
#
# If you want to stop if the counter is at 10, then use break (this will come out of the loop)
# This won't print 10
# for x in range(1,21):
#     if x==10:
#         break
#     else:
#         print(x)
# print("I predict the next number will be 10")
#
# ###########################################################################################################
# Countdown timer project
#
# import time
#
# time.sleep(3) #The code sleeps for 3 seconds. So the code will print after 3 seconds
# print("3 seconds have passed")
#
# timer = int(input("Enter your timer in seconds:"))
#
# while timer > 0:
#     print(timer)
#     time.sleep(1)
#     timer -= 1
# print("Your time is up")
#
# Digital clock style, using for loop
# my_time= int(input("Enter the time in seconds:"))
# for x in range (my_time, 0, -1):
#     seconds= x%60
#     minutes= int(x/60)%60
#     hours= int(x/3600)%60
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Your time is up")
#
# #####################################################################################
# Nester loops
# A loop inside another loop (outer, inner)
# outer loop:
#     inner loop
#
# Say you want to print numbers 1 to 9
# for x in range(1,10):
#    print(x)
# If you don't want them vertically, you can place them in the same line by using the end function:
# for x in range(1,10):
#     print(x, end="")
#
# If you want to print this 3 more times, nest this loop in a for loop. make sure to include different counters
# for x in range(1,4):
#     for y in range(1,10):
#         print(x, end="")
# The result will look like: 123456789123456789123456789. If you want to keep each iteration in a different line, in the indent of the outer loop add print() which prints a new line
#
# for x in range(1,4):
#     for y in range(1,10):
#         print(y, end="")
#     print()
#
#
# #
# Ex; 2:
# Making a rectangle using a symbol with dimension of the user's input
# We'll reuse some of the code we wrote above
#
# row = int(input("Enter the number of rows:"))
# coloumn = int(input("Enter the number of coloumns:"))
# symbol = input("Enter a symbol you want the rectangle to be made of:")
#
# The outer loop is rows and inner is coloumns
# for x in range(row):
#     for y in range(coloumn):
#         print(symbol, end="")
#     print()
#
# ###################################
# Collections
# single variable used to store multiple values
#     List= [] -- ordered and changeable. Duplicates are accepted
#     Set= {} -- unordered and not changeable, but you can add or remove stuff. No duplicates
#     Tuple= () ordered and unchangeable. Duplicates are fine. It is relatively faster to work with.
#
# var = (/{/[ 'element' , 'element' , ... ]/}/)
#
# Ex;
# fruits = ["apple","banana","orange","avocado"]
# print(fruits)
# To access an element, use the indexing operator
# print(fruits[0])
#
# You can also iterate over your list using loops:
# for x in fruits:
#     print(x)
#
# Use the in operator to return a boolean value if an element is in a list
# print("apple" in fruits)
#
# Methods for sets:
#
# Append; to add an element to the end of a set
# fruits.append("Kothi")
#
# Remove; to remove an element
# fruits.remove("apple")
#
# Insert; to insert at a given index
# fruits.insert(1, "plum")
#
# Sort; to sort
# fruits.sort()
#
# reverse
# fruits.reverse()
#
# Clear; remove everything
# fruits.clear()
#
# Index; to find the index of an element;
# print(fruits.index("apple"))
#
# Count; how many? cuz duplicates are allowed
# print(fruits.count("apple"))
#
# for x in fruits:
#     print(x)
#
# ______________#
#
# Sets
# fruits = {"apple", "orange", "banana", "coconut"}
# Unordered, not changeable, but can add and remove, no duplicate
# print(fruits)
# each time you print it, it will be randomized
#
# Methods for set
# print(len(fruits))
# print("pineapple" in fruits)
# There's no finding an index so no print(fruits[0])
# Add or remove:
# fruits.add("pineapple")
# fruits.remove("apple")
# print(fruits)
#
# fruits.pop()
# Removes the first one when printed, random of course
# print(fruits)
#
# fruits.clear()
#
# _____#
# Tuple
# If you don't care about having to change anything and still want order, then use tuple cuz its faster
# fruits = ("apple", "orange", "banana", "coconut")
# Methods;
# length
# in
# fruits.index("")
# fruits.count()
#
# ################################################################################################################################################
# Shopping cart program
#
# foods = []
# prices = []
# total = 0
# Setting everything empty so we can accept user input
# List is best because you can append stuff and it is in order
# while True:  #While the condition is True
#     food = input("Enter a food in your list. Once you're done, press 'q': ")
#     if food.lower() == "q":    #lower function because the user might add a Q instead of q
#         break #come out of the loop
#     else:
#         price = float(input(f"Enter the price of a {food}: $")) #asking the price of the food
#         foods.append(food) #Adding the food to the empty foods set
#         prices.append(price) #adding the price to the empty price set
# print()
# print(" YOUR CART: ")
#
# for food in foods:   #For every food, print the food in a new line
#     print(food)
#
# for price in prices:
#     total += price   #Total is the total + the price
#
# print(f"Your total is ${total}")

# ##########################################################################################################
# 2d lists
# Basically a list made up of lists
# Useful for grids/matrices
#
# fruits =     ["apple", "banana", "orange"]
# vegetables = ["potato", "carrot", "cabbage"]
# meat =       ["chicken", "mutton", "fish"]
#
# groceries = [fruits, vegetables, meat]
#
# If you want to access an element, think of the lists and elements as a coordinate system
# printing the zeroth element would mean to print the first row,
# printing the zeroth element and the 1st element would lead to 'banana', since it is at the corrdinates 0,1
# print(groceries[0][1])
#
# Another way you can make a 2d list is:
# groceries = [
#    ['apple', 'banana','orange'],
#    ['potato', 'carrot', 'cabbage'],
#    ['chicken', 'mutton', 'fish']
#             ]
# Putting the lists directly in the 2d list separated by commas
#
# If you want to iterate over a 2d list, use a nested loop
# Example, only using 1 loop:
#
# for collection in groceries:
#    print(collection)
# This would print each row
#
# for collection in groceries:
#    for item in collection:
#        print(item)
# This would print each element of each row
#
# If you want it to resemble a grid system:
# for collection in groceries:
#    for item in collection:
#        print(item, end=" ")
#    print()
# ############################################################
# 2d numberpad program
#
# Use tuple cuz it's ordered and faster
# 2d tuple:
#
# numberpad =  (
#        ('1','2','3'),
#        ('4','5','6'),
#        ('7','8','9'),
#        ('*','0','#')
# )
# for row in numberpad:
#    for number in row:
#        print(number, end=" ")
#    print()
# #############################################################
# Quiz game
#
# import time
#
# questions = ("Which direction does the Sun rise?:",
#             "What color is an apple?:",
#             "What is the molecular formula for oxygen gas?:",
#             "What is 1+1?:",
#             "Do aliens exist?:")
# options = (
#            ('A) North', 'B) East',   'C) West',  'D) South'),
#            ('A) Red',   'B) Yellow', 'C) Black', 'D) Blue'),
#            ('A) Fe2O3', 'B) O',      'C) Al2O3', 'D) O2'),
#            ('A) 3',     'B) 2',      'C) 1',     'D) Happy New Year'),
#            ('A) Yes',   'B) No',     'C) Maybe', 'D) I am an alien boi')
# )
#
# answers = ('B','A','D','B','C')
# guesses = []    #Using a set cuz we can append to the guesses
# score = 0
# q_num = 0
#
# for question in questions:
#    print("=====================================")
#    print(question)
#    for option in options[q_num]:      #Here, we are using the index of 0, which is set for the q_num variable, so the first question will display only the fist set of options
#        print(option, end=" ")
#        print()
#
#    guess = input("Enter the correct option (A, B, C, D):").upper()  #We are making all the inputs a capital letter
#    guesses.append(guess)                                            #We are adding the guess into the guesses list
#    if guess == answers[q_num]:        #If the guess matches the answer at the correct question number index
#        score+=1                       #Add one to the score
#        print("Correct")
#    else:
#        print("Wrong")
#        print(f"{answers[q_num]} is the correct answer")
#
#    time.sleep(1)                     #I imported the time module and added a small delay between the answer display and the next question for more clarity (I'm just smart like that)
#    q_num+=1                           #Inceasing the question number value by 1 each time so that the options are for the corresponding questions
#
# print()
# print("-------------------Results-------------------")
#
# print(f"Your final score is {score}/5 !")
# if 3<=score<=5:
#    print("You did well!")
# elif 1<=score<=3:
#    print("You could've done better")
# else:
#    print("You are intellectually challenged.")
#
# ____________________________#
# For further stuff, access main2.py

########################################################################################################################
# Making the Shopping cart program a bit better
# Mostly logic and readability improvements
#
#
# def decor(count):
#     print("=" * count)
#
#
# def main():
#     cart = []
#     prices = []
#     total = 0
#
#     decor(22)
#     print("Welcome to the PyShop!")
#     decor(22)
#
#     while True:
#         item = input("Enter an item in your list. Press 'q' to checkout: ").capitalize()
#         if item == "Q":
#             break
#         else:
#             cart.append(item)
#
#         while True:
#             try:
#                 price = float(input(f"Enter the price of {item}: $"))
#                 prices.append(price)
#                 break
#             except ValueError:
#                 print("That is not a valid price")
#
#     decor(12)
#     print(" YOUR CART: ")
#     decor(12)
#
#     print("Items:")
#     for item in cart:
#         print(item)
#
#     print("\nPrices:")
#     for price in prices:
#         print(f"${price}")
#         total += price
#
#     print(f"Your total is ${total}")
#     decor(28)
#     print("Thanks for PyShopping today!")
#
# if __name__ == '__main__':
#     main()