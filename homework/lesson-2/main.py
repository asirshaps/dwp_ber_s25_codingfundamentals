#String variables
my_number = 10
print(my_number)

my_string = "Hello Python"
print(my_string)

my_float = 3.14
print(my_float)
print('***************************')


#String Concatenation
first_name = "Asirsha "
last_name = "Padmanabhan Sivasankaran"
full_name = first_name  + last_name
print(full_name)
print('***********************************')

#Arithmetic Operations
a=5
b=3
add_result = a+b
sub_result = a-b
mult_result = a*b
div_result = a/b
print(add_result)
print(sub_result)
print(mult_result)
print(div_result)
print('**********************************')

#Boolean
# a. Creating boolean
is_greater = 5>3
is_equal = 5==3
is_smaller = 5<3
print('Boolean operations')
print("5>3 =", is_greater)
print("5==3 =", is_equal)
print("5<3 =", is_smaller)
print('*****************************************')

# b. Boolean operations
bool1 = True
bool2 = False
print('bool1 =', bool1)
print('bool2 =', bool2)
# AND
print('And operation')
a1 = bool1 and bool2
print('bool1 and bool2 = ', a1)
# OR
print('Or operation')
b1 = bool1 or bool2
print('bool1 or bool2 = ', b1)
# NOT
print('Not operation')
c1 = not bool1
d1 = not bool2
print("not bool1 =", c1)
print("not bool2 =", d1)
print('*****************************************')

# 4. COMPARISON BETWEEN DATATYPES
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"
# compare pi and pi_pi
3.14 == '3.14'
print(3.14 == '3.14')
# compare pi_pi and pi_pi_pi
3.14
'3.14' == "3.14"
print('3.14' == "3.14")

# Type checking and conversion
# a. Type checking
print(type(pi))
print(type(pi_pi))
print(type(pi_pi_pi))

#b. Type conversion

my_str = "123"
my_int = int(my_str)
my_float_converted = float(my_int)
print(my_str)
print(my_int)
print(my_float_converted)

#5. CHALLENGE
celsius = 37
fahrenheit = (celsius * 9/5) +32
print(celsius)
print(fahrenheit)
