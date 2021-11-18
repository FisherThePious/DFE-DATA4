#==================================================================================================
#   Allows you to enter a team name and then appends the team name to a new line.
#==================================================================================================
# print(str("=========================================\nWelcome to the Teams List editor\n========================================="))
# print(str("This script should allow you to edit the teams.txt file and append an inputted team.")) 
# while True:

#     teamfile = open("Python/file-manipulation/teams-exercise/teams.txt", "r+")
#     chars = teamfile.readline()
#     teamname = str(input("Please enter the name of the football team you wish to save:\n"))
#     #newline = (chars.append(teamname))
#     teamfile.write(teamname + "\n")
#     teamfile.close
#     check = input("Would you like to continue adding teams to the list?\nPress 'Y' to restart or any key to exit and press enter.\n")
#     if check.upper() == "Y":
#         continue
#     print("Thank you for using the teams editor!")
#     break
#==================================================================================================
#   Function used if it was a pre-determined list to be added to the text file.
#==================================================================================================
# with open("Python/file-manipulation/teams-exercise/teams.txt"), "w") as file
#
#     teamlist = ["Leeds United", "Manchester United", "Liverpool", "Chelsea", "Crystal Palace"]
#
#     for n in teamlist:
#         teamlist = teamlist + n + "\n"
#     file.write(teamlist)
#
#==================================================================================================
#   Should print the first and the last entry in the teams.txt
#==================================================================================================
myfile = open('Python/file-manipulation/teams-exercise/teams.txt', "r")
chars = myfile.readlines()
print(chars[0])
print(chars[-1])
