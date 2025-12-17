a = ["geeks", "geeksforgeeks", "geeky", "geek", "apple", "banana"]

# Prefix to match
prefix = "geeks"

# Initialize count
count = 0

# Loop through the list and check
# if each word starts with the given prefix
for word in a:
    if word.startswith(prefix):
        count += 1

print(f"The prefix '{prefix}' appears {count} times.")