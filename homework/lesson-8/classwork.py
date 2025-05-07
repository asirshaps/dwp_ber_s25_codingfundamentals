personal_info_dictionary = {"name" : "Asirsha",
                            "age" : 29,
                            "occupation" : "Student"
                            }
print(personal_info_dictionary)
# add hobby to dictionary
personal_info_dictionary["hobby"] = "Craft work"
print(personal_info_dictionary)
# print occupation using get()
print(personal_info_dictionary.get("occupation"))
# ---- OR ----
# print occupation using method of calling the key
print(personal_info_dictionary["occupation"])
# add nationality to dictionary
personal_info_dictionary["nationality"] = "Indian"
print(personal_info_dictionary["nationality"])
# print "unknown if there is no nationality"
print(personal_info_dictionary.get("Nationality", "Unknown"))
#print(personal_info_dictionary["nationality"])
# print all the keys
print(personal_info_dictionary.keys())
# print all the values
print(personal_info_dictionary.values())
# update the "occupation"
personal_info_dictionary["occupation"]= "Chef"
print(personal_info_dictionary)
# remove age
personal_info_dictionary.pop("age")
# ---- OR ----
#del personal_info_dictionary["age"]
print(personal_info_dictionary)
#check "Favourite color" in personal_info_dictionary
if "favourite colour" in personal_info_dictionary :
    print(personal_info_dictionary.get("favourite colour"))
else :
    print("not present")

# ex 2
incomes = {"Mother": 3600.00, 
           "Father": 2500.00, 
           "Daughter": 500.00
           }
print(incomes)
total_income = 0
for value in incomes.values() :
    total_income += value
print("THe total income in the family -" , total_income)


## Example
my_dict = {"name" : "Rapunzel" ,
           "age" : 19 ,
           "hobbies" : ["painting" , "reading" , "singing"]}


# Using the dictionary my_dict , convert the dictionary into a list of tuples using a for loop. (hint: use the method append()) 
my_dict_list = []
for item in my_dict.items() :
    my_dict_list.append(item)
print("The required converted list -",my_dict_list)
print("******************************************************************")

# Create dictionaries similar to the Rapunzel one for you and 2 of your friends. Create a list of
# dictionaries with both information ( myList = [ my_dict, my_friend_dict_1 ,my_friend_dict_2] . 
# Calculate the average of all your ages. 
my_dict = {"name" : "Rapunzel" ,
           "age" : 19 ,
           "hobbies" : ["painting" , "reading" , "singing"]}

my_friend_dict1 = {"name" : "Arya" ,
           "age" : 18 ,
           "hobbies" : ["Cooking" , "travel" , "writing"]}

my_friend_dict2 = {"name" : "Nandana" ,
           "age" : 29 ,
           "hobbies" : ["dancing" , "photoshop editing" , "stitching"]}

'''Printing items in my_dict '''
for item1 in my_dict.items() :
    print(item1)

'''Printing items in friend1'''
for item1 in my_friend_dict1.items() :
    print("Friend 1 details : ")
    print(item1)

'''Printing items in friend2'''
for item1 in my_friend_dict2.items() :
    print("Friend 2 details : ")
    print(item1)

'''Printing items in all three'''
my_list = []
for item1 in my_dict,my_friend_dict1,my_friend_dict2 :
            my_list.append(item1)
print("The whole list of 3 friends - ",my_list)

# calculate the average of ages
total_of_age = 0
length = len(my_list)
for item in my_dict,my_friend_dict1,my_friend_dict2 :
     print(item)
     print(item.get("age"))
     
     total_of_age += item.get("age")
average = total_of_age/length
print("The average of all your ages - " , average)