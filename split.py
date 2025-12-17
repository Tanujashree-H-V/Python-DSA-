a = ['Gfg is best', 'for Geeks', 'Preparing for Placement']

# Character to split on (space)
k = ' '

# Initialize an empty list to store the result
res = []

# Loop through each string in the list
for word in a:
  
    # Split the string at each space 'K'
    split_word = word.split(k)
    res.append(split_word)

print(res)