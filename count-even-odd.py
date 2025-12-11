# Creating a list of numbers
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Initializing counters for even and odd numbers
even = 0
odd = 0

for num in a:
  
    # Checking if the number is even
    if num % 2 == 0:  
        even += 1
    else:  
        odd += 1

# Printing the results
print("Even numbers:", even)
print("Odd numbers:", odd)