#--------------------------------------------------------------------------------------------------------
#Using a list within the loop to append
#--------------------------------------------------------------------------------------------------------
#count = 0
#friends =[]

#while count < 5:
#    name = input("Enter your name: ")
#    friends.append(name)
#    count += 1

#for friend in friends:
#    print(friend, "is awesome")

#--------------------------------------------------------------------------------------------------------
#Finds multiples of 5 and 7 between 1500 and 2700
#--------------------------------------------------------------------------------------------------------
#multiples=[]
#
#for meme in range(1500, 2700):
#    if (meme%5==0) and (meme%7==0):
#        multiples.append(str(meme))
#print (multiples)

#--------------------------------------------------------------------------------------------------------
#Calculator which converts temperature between two units
#--------------------------------------------------------------------------------------------------------
unit = 0 #This determines whether Farenheit or Celcius
measurement = 0 #This is the temperature
conversion = 0 #This is the output

while unit == 0:
    unit = int(input("Please select the unit of measurement you wish to convert from\n[1]Celsius\n[2]Farenheit\nType option below\n"))
    if unit == 1:
        measurement = int(input("Please enter your temperature in °C:\n"))
        conversion = int(round(measurement / 5 * 9 + 32))
        print(measurement, "°C is equivalent to", conversion, "°F" )
    elif unit == 2:
        measurement = int(input("Please enter your temperature in °F:\n"))
        conversion = int(round((measurement - 32) * (5 / 9)))
        print(measurement, "°F is equivalent to", conversion, "°C" )
    else:
        print("You have selected an invalid option, please try again.")
        quit

#--------------------------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------------------
