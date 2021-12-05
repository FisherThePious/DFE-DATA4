#===================================================================================================
#   Exercise 1: Mailing Address   
#   Create a program that displays your name and complete mailing address formatted in
#   the manner that you would usually see it on the outside of an envelope. Your program
#   does not need to read any input from the user.                                                                |
#===================================================================================================
#print("Jordan Fisher\njordanfisher@email.com\n123 Street Name, City, Country")
#===================================================================================================
#    Exercise 2: Hello World
#    Write a program that asks the user to enter his or her name. The program should
#    respond with a message that says hello to the user, using his or her name                                                                  |
#===================================================================================================
#name = str(input("Please enter your name below\n"))
#print("Hello", name)
#===================================================================================================
#   Exercise 3: Area of a Room  
#   Write a program that asks the user to enter the width and length of a room. Once
#   the values have been read, your program should compute and display the area of the
#   room. The length and the width will be entered as floating point numbers. Include
#   units in your prompt and output message; either feet or meters, depending on which
#   unit you are more comfortable working with                                                              |
#===================================================================================================
# room_width = float(input("Please enter the width of the room in feet:\n"))
# room_length = float(input("Please enter the length of the room in feet:\n"))
# area_formula = room_width * room_length
# print (f"The area of the room is {area_formula}ft²")
#===================================================================================================
#   Exercise 4: Area of a Field  
#   Create a program that reads the length and width of a farmer’s field from the user in
#   feet. Display the area of the field in acres.                                                         |
#===================================================================================================
# field_width = float(input("Please enter the width of the field in feet:\n"))
# field_length = float(input("Please enter the length of the field in feet:\n"))
# area_formula = field_width * field_length
# acre_conversion = area_formula/43560
# print (f"The area of the field in acres is {acre_conversion} acre(s)")
#===================================================================================================
#   Exercise 5: Bottle Deposits
#   In many jurisdictions a small deposit is added to drink containers to encourage people
#   to recycle them. In one particular jurisdiction, drink containers holding one liter or
#   less have a $0.10 deposit, and drink containers holding more than one liter have a
#   $0.25 deposit.
#   Write a program that reads the number of containers of each size from the user.
#   Your program should continue by computing and displaying the refund that will be
#   received for returning those containers. Format the output so that it includes a dollar
#   sign and always displays exactly two decimal places.                                                      |
#===================================================================================================
# large_bottle = float(input("Please enter the number of containers that hold 1L or more:\n"))
# small_bottle = float(input("Please enter the number of containers that hold less than 1L:\n"))
# large_return = 0.25
# small_return = 0.10
# total_return = (large_bottle*large_return) + (small_bottle*small_return)
# monetised = round(total_return, 2)
# print (f"Your total returns for your containers is ${monetised}.")
#===================================================================================================
#   Exercise 6: Tax and Tip
#   The program that you create for this exercise will begin by reading the cost of a meal
#   ordered at a restaurant from the user. Then your program will compute the tax and
#   tip for the meal. Use your local tax rate when computing the amount of tax owing.
#   Compute the tip as 18 percent of the meal amount (without the tax). The output from
#   your program should include the tax amount, the tip amount, and the grand total for
#   the meal including both the tax and the tip. Format the output so that all of the values
#   are displayed using two decimal places.
#===================================================================================================
# pretax_amount = round(float(input("Please anter the price of the customer's meal:\n")),2)
# service_charge = round(0.18 * pretax_amount,2)
# taxable_amount = round(pretax_amount - service_charge,2)
# tax_deduction = round(0.05 * taxable_amount,2)
# final_bill = round(taxable_amount - tax_deduction,2)
# print('Total Amount: ${:,.2F}'.format(pretax_amount),'\nService Charge: ${:,.2F}'.format(service_charge),'\n5% VAT: ${:,.2F}'.format(tax_deduction),'\nAfter Tax Cost: ${:,.2F}'.format(final_bill))
#===================================================================================================
#   Exercise 7: Sum of the First n Positive Integers
#   Write a program that reads a positive integer, n, from the user and then displays the
#   sum of all of the integers from 1 to n. The sum of the first n positive integers can be
#   computed using the formula:        
#===================================================================================================