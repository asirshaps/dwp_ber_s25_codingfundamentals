quota = 1000
value = int(input("Enter a value "))
if value >= quota :
    print("Done")
else :
    print("Not Done")

result = quota - value
if value >= quota :
    print(0)
else :
    print(result)

def fruits_remaining(fruits_picked ,fruits_quota) :
    if fruits_picked >= fruits_quota :
        return 0
    else :
         return fruits_quota - fruits_picked
fruit = fruits_remaining(23,30)
print(fruit)
fruit1 = fruits_remaining(1,1)
fruit2 = fruits_remaining(100,117)
fruit3 = fruits_remaining(0,-9)
print(fruit1 , fruit2 , fruit3)

def is_friday_off (fruit_picks,fruits_quota) :
   total_picked = sum(fruit_picks)
   return total_picked >= fruits_quota 

fruit_picks_1 = [223, 212, 202, 234]
fruit_picks_2 = [200, 256, 189, 240]
quota = 880
print(is_friday_off(fruit_picks_1,quota))
print(is_friday_off(fruit_picks_2,quota))