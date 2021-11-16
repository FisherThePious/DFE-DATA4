var1 = input("Enter the first number: ")
#var2 = input("Enter the second number: ")
first_number = int(var1)
#second_number = int(var2)

# if first_number < second_number:
#     print (var1, "is less than", var2)
# elif first_number == second_number:
#     print (var1, "is equal to", var2)
# else:
#     print (var1, "is more than", var2)


if first_number >= 0 and first_number <= 100:
    if first_number >= 85:
        print("Distinction")
    elif first_number >= 65 and first_number <= 84:
        print("Pass")
    else:
        print("Fail")
else:
    print ("You have entered an invalid score, please try again.")
