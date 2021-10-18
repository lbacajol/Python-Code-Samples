# Leslie Bacajol
# October 12, 2021

#Problem 1 
# This programs prints "Hello World"
print("Hello World")

#Problem 2
#This Programs asks the user for their name then greets them with their name
name= input("Hello, what is your name?")
print("Hi there, " + name) 

#Problem 3
#This program greets only the user, their intructor and myself with our names 
name1= input("What is your name?")
name2= input("What is your instructor name?")
myname= ",I am Leslie" 
print("Hi there, " + name1 + " " + "and" + " " + name2 + myname)

#Problem 4
#This program computes the area of a circle, by the user entering the radius of the circle then it tells them the answer
Pi = 3.147
r = float (input("What is the radius of your circle?"))
area = Pi * r * r
print(" The area of your circle is = %.2f" %area)


#Problem 5
#This program will compute MPG for a car, by the user entering the number of miles driven and the number of gallons used then it tells them the answer
Miles = int(input("Current Car Miles: "))
Gallons = int(input("Gallons Used: "))
print("Thank you for inputing the information, your MPG is: ", Miles/Gallons)

#Problem 6
#This program converts degrees Fahrenheit to degrees Celsius
fahrenheit = float(input(" What is the temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print ('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

#Problem 7
#This program calculates which number of the day of the week you will return on after vacations
#the user enters the starting day number, the length of their stay
# the name of the days is 0-6 where day 0 is sunday and day 6 is saturday
start_day = int(input("from 0-6 what day is it?"))
days_to_wait = int(input("How many days are you going to be gone for?"))
end_day = (start_day + days_to_wait)
print (end_day)

