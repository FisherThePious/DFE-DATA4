myfile = open('README.md')
chars = myfile.readlines()
myfile.close
chars.insert(2,"This is an edit\n")
chars.append("This is an appended edit\n")
print(chars)