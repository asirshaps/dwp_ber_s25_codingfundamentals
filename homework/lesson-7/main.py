# SHOPPING LIST
shopping_set = set()
while True :
    items = input("Enter your item ").strip()
    if items.lower() == "done" :
      break
    if not items :
        continue
    shopping_set.add(items)
shopping_list = list(shopping_set)    
shopping_list.sort()
for index,s in  enumerate(shopping_list) :
       print(index + 1,s)
length = len(shopping_list)
print("Total no.of items " ,length )  