import re

name = 'Python is 1'
name1 = "counting digits, letters and spaces in a string"

digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall("[ \s]", name)

digitCount1 = re.sub("[^0-9]", "", name1)
letterCount1 = re.sub("[^a-zA-Z]", "", name1)
spaceCount1 = re.findall("[ \s]", name1)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))

print("")

print(len(digitCount1))
print(len(letterCount1))
print(len(spaceCount1))