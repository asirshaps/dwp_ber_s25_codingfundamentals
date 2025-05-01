#Exercise 1
#A - The built-in function in the random module that generates random integers is called randint().

# B
from random import randint
import random
rand_numbers = []
for _ in range(1,11):  # Repeat 10 times
    #print(random.randint(1, 100))
    n = random.randint(1,100)
    rand_numbers.append(n)
print("10 random numbers are ",rand_numbers)

def average(a):
    avg = sum(a)/10
    print("Average of 10 random numbers are ",avg)
average(rand_numbers)

# C
import statistics
print("10 random numbers are ",rand_numbers)
avg_builtin = statistics.mean(rand_numbers)
print("Average of 10 random numbers using builtin function is ",avg_builtin)

# D - The result of B and C are same

#Exercise 2
def addition(a,b) :
    return a + b
def subtraction(a,b) :
    return a - b
def multiplication(a,b) :
    return a * b
def division(a,b) :
    if b != 0 :
        return a / b
    else :
        return "division not possible"
raw_input1 = input("Enter a number ")
if not raw_input1.isdigit()  :
    print("Invalid Input")
    exit()
raw_input2 = input("Enter a number ")
if not raw_input2.isdigit()  :
    print("Invalid Input")
    exit()
input1 = int(raw_input1)  
input2 = int(raw_input2)   
input3 = input("Enter operation ")

if input3 == "+" :
    add = addition(input1,input2)
    print(add)
elif input3 == "-" :
    sub = subtraction(input1,input2)
    print(sub)
elif input3 == "*" :
    mul = multiplication(input1,input2)
    print(mul)
elif input3 == "/" :
    div = division(input1,input2)
    print(div)
else :
    print("Invalid operation !")



# Exercise 3
from random import randint
# function to get computer guess
def random_numbers() :
    return randint(1,100)


# Function to get user guess
def guess() :
    input1 = int(input("What is your guess? "))
    return input1


# Function to compare , send user guess and computer guess , will get response as output
def check(user_guess , computer_guess) :
    if user_guess == computer_guess :
        return "Correct!"
    elif user_guess > computer_guess :
        return "Too high"
    else :
        return "Too low"
    
# Get Computer guess
computer_guess = random_numbers()

# Get user guess 5 times and compare each and print response
for u in range(5) :
    input_guess = guess()
    result = check(input_guess,computer_guess)
    print(result)
    if result == "Correct!" :
        print("You won at ",u,"th attempt")
        exit()
        
print("You lose")
