#Find numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#multiples=[]
#
#for meme in range(1500, 2700):
#    if (meme%5==0) and (meme%7==0):
#        multiples.append(str(meme))
#print (multiples)

#Conversion of temperatures to and from celcius and farenheit.
unit = 0 #This determines whether Farenheit or Celcius
measurement = 0 #This is the temperature
conversion = 0 #This is the output

while unit == 0:
    unit = int(input("Please select the unit of measurement you wish to convert from\n[1]Celsius\n[2]Farenheit\nType option below\n"))
    if unit == 1:
        measurement = int(input("Please enter your temperature in °C:\n"))
        conversion = measurement / 5 * 9 + 32
        print(measurement, "°C is equivalent to", conversion, "°F" )
    elif unit == 2:
        measurement = int(input("Please enter your temperature in °F:\n"))
        conversion = (measurement - 32) * (5 / 19)
        print(measurement, "°F is equivalent to", conversion, "°C" )
    else:
        print("You have selected an invalid option, please try again.")
        quit