# 1. Basic Arithmetic Operations
print(" Basic Arithmetic Operations")
input1 = input("Enter any number : ")
converted_input1 = int(input1)
input2 = input("Enter any number : ")
converted_input2 = int(input2)
#addition
add_result = converted_input1 + converted_input2
print("Additon - ",add_result)

#subtraction
sub_result = converted_input1 - converted_input2
print("Subtraction - ",sub_result)

#multiplication
mul_result = converted_input1 * converted_input2
print("Multiplication - ",mul_result)

#division
div_result = converted_input1 / converted_input2
print("Division - ",div_result)

# 2. Modulus and Exponentiation
print(" Modulus and Exponentiation")
input3 = input("Enter a number ")
converted_input3 = int(input3)
modulus = converted_input3 % 3
exponent = converted_input3 ** 2
print("Remainder of ",converted_input3, "by 3 is ", modulus)
print(converted_input3," to the power of 2 is ", exponent)

# 3. Odd or Even
print("Odd or Even")
input4 = input(" Enter a number ")
converted_input4 = int(input4)
if converted_input4 % 2 == 0 :
    print(converted_input4 , " is even")
else :
    print(converted_input4 , " is odd")


# 4. Compare Two Numbers
print("Compare Two Numbers")
input5 = input(" Enter a number ")
input6 = input(" Enter a number ")
converted_input5 = int(input5)
converted_input6 = int(input6)
if converted_input5 > converted_input6 :
    print("The first number is greater than the second")
elif converted_input6 > converted_input5 :
     print("The second number is greater than the first")
else :
    print(" The two numbers are equal")


# 5. Print Numbers 1 to 10
print("Print Numbers 1 to 10")
for input7 in range(1,11) :
    print(input7)


# 6. Multiplication Table
print("Multiplication Table")
input8 = input(" Enter a number ")
converted_input8 = int(input8)
for i in range (1,11) :
    result = converted_input8 * i
    print(converted_input8, " x " , i,"=" , result)


# Bonus Questions 

# 7. FizzBuzz
print("FizzBuzz")
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else :
        print(i)


# 8. Leap year
print("Leap year")
input10 = input("Enter an year ")
converted_input10 = int(input10)
if converted_input10 % 100 == 0  and converted_input10 % 400 == 0  :
    print(converted_input10 ," is a leap year")
elif converted_input10 % 4 == 0 and converted_input10 % 100 !=0 :
    print(converted_input10 ," is a leap year")
else :
    print(converted_input10 ," is not a leap year")

