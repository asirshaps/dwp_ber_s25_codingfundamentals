# Exercise 0
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
length = len(scores)
print(scores)
print("Length of the list is - ",length)

# Exercise 1:
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
no_of_3 = scores.count(3)
print("The no.of 3 in the list is " , no_of_3)

# Exercise 2:
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
maximum = max(scores)
print("The maximum value in the list is " , maximum)

# Exercise 3:
list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]
set_list_1 = set(list_1)
set_list_2 = set(list_2)
print(set_list_1)
print(set_list_2)
common_elements = set_list_1.intersection(set_list_2)
print("The common elements in both lists are ", list(common_elements))
# You can find the common elements without converting to set 
for item in list_1 :
    if item in list_2 :
        print(item)

# Exercise 4:
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
print(all_numbers)
positive_numbers = []
for number in all_numbers :
    if number > 0 :
        answer = number
        positive_numbers.append(answer)
print("The new list with positive numbers -", positive_numbers)

# Exercise 5:
reverse_this_list = [10, 20, 30, 40, 50]
print(reverse_this_list)
reverse_this_list.reverse()
print( "The reversed list is ", reverse_this_list)

# Exercise 6:
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print(scores)
set_scores = set(scores)
print("The converted set - " , set_scores)

# Exercise 7:
country1 = ("India" , "New Delhi")
country2 = ("Germany" , "Berlin")
country3 = ("Italy" , "Rome")
country4 = ("Austria" , "Vienna")
country5 = ("United Kingdom" , "London")
list = [country1 , country2 , country3 , country4 , country5]
print("The list of tuples with countries and their capitals are as follows :- ")
print(list)
