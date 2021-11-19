#-----------------------------------------------------------------------------------------------------
#   Data Structures: Lists, Dictionaries and Tuples
#-----------------------------------------------------------------------------------------------------
dog_dict = {"Scooby": "Scared", "Snoopy": "Fighting the Red Baron"}
dog_dict2 = {"Scrappy": "Angry", "Brian": "Hipster"}
dog_dict2 |= dog_dict #the |= updates the first dictionary with the entries from the second.

for i in dog_dict2:
    print(i)

#dog_dict2.clear() #Uncommenting this will clear the dictionary with an error returned

print(dog_dict2["Scrappy"], "<- This should return Angry")
print(dog_dict2["Scooby"], "<- This should return Scared")

del dog_dict2["Brian"] # Delete's the Brian entry from the dictionary so shouldn't print.

tup = dog_dict2.items() # items allows us to return the pairs as tuples
print(tup) 
#-----------------------------------------------------------------------------------------------------
# example_dict = {"name": "Steven", "city": "London", "age": 34}
# print(example_dict.get("name"))
# print(example_dict.get("city"))
# print(example_dict.get("age"))
#-----------------------------------------------------------------------------------------------------