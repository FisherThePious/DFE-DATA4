myfile = open('README.md')
chars = myfile.readlines() #reads an entire line into the variable - remembers how far it's gone into doc
myfile.close
chars.insert(2,"This is an edit\n")
chars.append("This is an appended edit\n")
print(chars)