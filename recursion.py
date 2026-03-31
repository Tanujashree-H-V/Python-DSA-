def sum_of_n(n):
    """
    Recursively calculates the sum of the first n numbers.
    
    Args:
        n: A positive integer
    
    Returns:
        The sum of numbers from 1 to n
    """
    if n <= 0:
        return 0
    return n + sum_of_n(n - 1)


# Example usage
print(sum_of_n(5))   # Output: 15
print(sum_of_n(10))  # Output: 55