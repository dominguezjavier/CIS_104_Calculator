import calculator




#provided a greeting to encourage the user to input thier required information.
print("Hello and welcome to our fun and simple calculator. Enjoy your time here.")

#I felt that asking the user to input a number first was the right way to start the calculator.
#Not sure how to incorporate the power or invert function if it is used here. Will ask if it doesn't come out working correctly.
num1 = input( 'Please enter the first number: ')

#I am not sure if I should include the invert or power sign here? Will ask for help from our class.
print("Now please be so kind to select an operation you would like to perform." )
operation = input(" \
Please type in the math operation you would like to complete: \
+ for add \
- for subtract \
* for multiply \
/ for divide \
** for power function \
% for modulo \
c for clear \
r for recall \
s for storage \
i for invert \
x for exit :")

#This is where I felt the right order/sequence to ask for the second number to be input into the equation
num2 = input( 'Please enter the second number: ')
while(operation!= 'x'):

#Here is where I am starting the conditional statements. I am frustrated at this point and feel like I am doing this wrong.
    if operation == '+':
        print('{} + {} = '. format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '. format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {}'. format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {}'. format(num1, num2))
        print(num1 / num2)
    # I got the concept for this set up from https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3
    
    elif operation == 'c':
        calculator.current_memory

    elif operation == 'r':
        calculator.recall

    elif operation == 's':
        calculator.cur_stor

    elif operation == 'i':
        calculator.invert

    elif operation == 'x':
        calculator.current_memory

    else:
        print('You have not entered a valid operator, please run the program again')

# I am not sure if I truly understand this project and the method correctly. 
# I will ask Lindsey and Jesse for some clarity and help.






 