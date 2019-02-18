#python program for a simple calculator
from cmath import exp  #Utilized this method from Trey's advice on looking up Cmath functions online



#function to add two numbers
def add(num1, num2):
    return num1 + num2
    
#function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

#function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

#function to divid two numbers
def divide(num1, num2):
    return num1 / num2

#function to raise a number to a power
def power(num1, num2):
    return num1** num2
# the ** is just an operator symbol that allows a function to happen. You do not need to include any other function on here

#function to store the calculator's current value
def cur_stor(num1):
    return num1

#function to recall and change the calculators current value to whatever is in the memory value, and returns the new current value
def recall(stored): #Wes explained that I would create a function in Main.py and reference it here as the recall. Thanks Wes and Jeremy 
    return stored

#function to clear the memory value
def clr():
    global stored
    stored = 0.0

#function to invert the calculators current value, and return the calculators new value
def invert(num1):
    num1 = num1 * -1
    return num1