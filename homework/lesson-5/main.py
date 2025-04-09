# Exercises on Functions and Imports

## HOMEWORK 1: Google time
from datetime import datetime

def print_current_datetime():
    now = datetime.now()
    print("Current Date and Time:", now)
print_current_datetime()


## HOMEWORK 2
string = input("Enter a string ")
def count_function(string):
    count = 0
    for c in string :
        count = count + 1
    print( "number of letters in the inputed string",string, "is"  ,count)
count_function(string)

# return statement
string = input("Enter a string ")
def count_function(string):
    count = 0
    for c in string :
        count = count + 1
    return count
number_of_letters = count_function(string)
print(number_of_letters)


## HOMEWORK 3: Using results of function in another function
def addition(a,b):
    add = a + b
    return add
input1 = int(input("Enter first number "))
input2 = int(input("Enter second number "))
add_result = addition(input1,input2)   # variable created to store function 
print(add_result)

def divisible_by_3(c):
    if c % 3  == 0 :
        print(c , "is divisible by 3")
    else :
        print(c , "is not divisible by 3")
divisible_by_3(add_result)


## (Bonus) HOMEWORK 4: Rock, Paper, Scissors
from random import randint
def play_game(user_choice) :
    computer_choice = randint(0,2)
    print(computer_choice)
    if user_choice == computer_choice :
        return "Tie"
    elif user_choice == 0 and computer_choice == 1 :
        return "You Lose"
    elif user_choice == 0 and computer_choice == 2 :
        return "You Win"
    elif user_choice == 1 and computer_choice == 0 :
        return "You Win"
    elif user_choice == 1 and computer_choice == 2 :
        return "You Lose"
    elif user_choice == 2 and computer_choice == 1 :
        return "You Win"
    elif user_choice == 2 and computer_choice == 0 :
        return "You Lose"
user_input = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors ")) 
result = play_game(user_input)
print(result)