'''
Created on Mar 16, 2020

@author: ITAUser
'''

'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract(num1, num2):
    subtractTwoNumbers = num1 - num2
    return subtractTwoNumbers
#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def divide(num1):
    divideANumber = ((num1/2)*77)+10000
    return divideANumber

#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def equality_check(num1, num2):
    if(num1>num2):
        print(False)
    else:
        print(True)

#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def number_check(num1, num2):
    if(num1 = num2):
        print(num1)
    if(num1>num2):
        print(num1)
    else:
        print(num2)
    
        
#5) Define a function that takes in two words and returns a string that contains both words combined.
def word_combine(string1, string2):
    wordCombination = (string1 + string2)
    return wordCombination
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def numbers_addition(num1, num2, num3):
    if(num1 = num2) or (num1 = num3)
        print(True)
    else:
        print(False)
#7) Define a function that prints your name.
def name_printing(string1):
    print(string1)
#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def color_favoritism(string1):
    if(string1 = "Blue"):
        print("That's my favorite color!")
    else:
        print("That is not my favorite color. Try again.")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def number_not0_loop(num1):
    if(num1 != 0)
    num1 = (num1-1)
    else:
    if(num1 = 0)
        print("The number is 0.")
        

'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.

#Personal Function) Create a function that makes negative numbers positive
def value_swap(num1):
    if(num1 < 0):
        print(num1+(num1*-2))
    else:
        print("The number is positive.")
