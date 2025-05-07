european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]

european_cities_info = {}
for key,value in european_cities :
    european_cities_info[key] = value
#print(european_cities_info)
for k,v in european_cities_info.items() :
    print(k,"-->",v)
european_cities_info = dict(sorted(european_cities_info.items()))
print(european_cities_info["Berlin"])
print(type(european_cities_info["London"]))
print(european_cities_info.get("Barcelona" , "Not Found"))
european_cities_info["Rome"] = [2870500, "Pasta", "Colosseum"]
european_cities_info.pop("Madrid")
print(european_cities_info)
output = "Amsterdam" in european_cities_info
if output :
    print("Amsterdam is there")
else :
    print("Amsterdam is not there")


dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"] 
countries = ["Italy", "Germany", "Spain", "USA"]
dishes_and_countries = dict(zip(dishes, countries))
print(dishes_and_countries)
