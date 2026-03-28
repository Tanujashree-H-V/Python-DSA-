vowels="aeoui"

s="hi tanu"
count=0
for i in s:
    if i in vowels:
        count+=1
print("number of vowels in the string are:", count)