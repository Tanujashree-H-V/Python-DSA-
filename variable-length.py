def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

# Example usage:
print(average(1, 2, 3, 4, 5))  # Output: 3.0
print(average())               # Output: 0