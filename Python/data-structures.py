#-----------------------------------------------------------------------------------------------------
#   Data Structures: Dictionaries, Lists and Tuples
#-----------------------------------------------------------------------------------------------------
# dog_dict = {"Scooby": "Scared", "Snoopy": "Fighting the Red Baron"}
# dog_dict2 = {"Scrappy": "Angry", "Brian": "Hipster"}
# dog_dict2 |= dog_dict #the |= updates the first dictionary with the entries from the second.

# for i in dog_dict2:
#     print(i)

# #dog_dict2.clear() #Uncommenting this will clear the dictionary with an error returned

# print(dog_dict2["Scrappy"], "<- This should return Angry")
# print(dog_dict2["Scooby"], "<- This should return Scared")

# del dog_dict2["Brian"] # Delete's the Brian entry from the dictionary so shouldn't print.

# tup = dog_dict2.items() # items allows us to return the pairs as tuples
# print(tup) 
#-----------------------------------------------------------------------------------------------------
# example_dict = {"name": "Steven", "city": "London", "age": 34}
# print(example_dict.get("name"))
# print(example_dict.get("city"))
# print(example_dict.get("age"))
#-----------------------------------------------------------------------------------------------------
# leeds_lst = ["Seacroft", "Horsforth", "Meanwood", "Headingley", "Holbeck"]
# reverse = leeds_lst.reverse()
# print(leeds_lst)
# leeds_lst.append("Crossgates") #appends Crossgates to the end of the list.
# print(leeds_lst)
# leeds_lst.remove("Seacroft") #appends Crossgates to the end of the list.
# print(leeds_lst[0]) #prints the first entry in the index
# print(leeds_lst[-1]) #prints the last entry in the index
# print(leeds_lst)
# print(reverse)
#-----------------------------------------------------------------------------------------------------