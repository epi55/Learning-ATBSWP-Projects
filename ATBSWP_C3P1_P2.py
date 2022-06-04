# The Collatz Sequence and Input Validation (Chapter 3, Project 1 and 2)
# Source: Automate the Boring Stuff With Python

'''
Question
The Collatz Sequence: Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

Input Validation: Add try and except statements to the previous project to detect whether the user types in a noninteger string.
'''
     
def collatz(number):
    if number % 2 == 0: # Determines if number is even, using modulo
        print("The number you entered, " + str(number) + ", is even!")
        print(int(number / 2)) # Int() to correct for float due to division
    elif number % 2 == 1: # Determines if number is odd, using modulo
        print("The number you entered, " + str(number) + ", is odd!")
        print(int(3 * number + 1)) # Int() to correct for float due to division (not needed)
    else:
        print("I'm uncertain what happened...") # Should never be printed, why was it?
    
    print("Let's put that number (" + str(number) + ") through the collatz sequence.")
    
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            print(int(number))
        else:
            number = 3 * number + 1
            print(int(number))
    
# Input request, running function, and ValueError exception
print("What is your number?")
try:
    number = int(input())
    collatz(number)
except ValueError:
    print("Your input cannot be used in the function. Please use numerals.")
