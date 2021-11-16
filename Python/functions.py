#=====================================================================================================
#   Input and greeting function
#=====================================================================================================
#def greeting(firstname, secondname):
#    return f"Hello {firstname} {secondname}"
#
#firstname = str(input("Please enter your first name:\n"))
#secondname = str(input("Please enter your last name:\n"))
#
#print(greeting(firstname, secondname))
#
#=====================================================================================================
#   Grading System
#=====================================================================================================
while True:

    def average_mark(homework, assessment, exam):
        mark_percentile = int(((homework + assessment + exam)/175) * 100)
        return int(mark_percentile)

    def grade_boundaries(mark_percentile):
        if mark_percentile >= 90 and mark_percentile <= 100:
            finalgrade = str("A")
        elif mark_percentile >= 70 and mark_percentile <= 89:
            finalgrade = str("B")
        elif mark_percentile >= 50 and mark_percentile <= 69:
            finalgrade = str("C")
        elif mark_percentile >= 30 and mark_percentile <= 49:
            finalgrade = str("D")
        elif mark_percentile >= 20 and mark_percentile <= 29:
            finalgrade = str("E")
        else:
            finalgrade = str("F")
        return str(finalgrade)

    firstname = str(input("Please enter the student's first name:\n"))
    secondname = str(input("Please enter the student's last name:\n"))
    homework = int(input("Please enter the students marks for homework:\n"))
    assessment = int(input("Please enter the students marks for assessment:\n"))
    exam = int(input("Please enter the students marks for final exam:\n"))

    mark_percentile = average_mark(homework,assessment,exam)
    finalgrade = grade_boundaries(mark_percentile)
    print(f"Student Name: {firstname} {secondname}\nFinal Marks: {mark_percentile} Final Grade {finalgrade}")
    check = input("Would you like to continue using the calculator?\nPress 'Y' to restart or any key to exit\n")
    if check.upper() == "Y":
        continue
    print("Thank you for using the grading calculator")
    break
#=====================================================================================================