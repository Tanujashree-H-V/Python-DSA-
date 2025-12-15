def reverse_in_groups(arr, k):
    n = len(arr)
    if k >= n:
        return arr[::-1]
    for i in range(0, n, k):
        arr[i:i+k] = reversed(arr[i:i+k])
    return arr
arr=[3,6,4,8,7]
k=4
print(reverse_in_groups(arr, k))
