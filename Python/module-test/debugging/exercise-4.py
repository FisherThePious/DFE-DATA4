# import pdb
# pdb.set_trace()

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 1

while n < 5:
    for i in item_list:
        print(*item_list, sep='\n')
        n += 1

print (item_list[4])