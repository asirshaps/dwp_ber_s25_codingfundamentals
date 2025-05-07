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
total_income = 0
for income in incomes.values() :
    total_income =total_income + income
print(total_income)
print(incomes)
my_dict = []
# add everything to list
# my_dict["Mother"] = 3600.00
# my_dict["Father"] = 2500.00
# my_dict["Daughter"] = 500.00
# print(my_dict)
for key , val in incomes.items() :
    # append