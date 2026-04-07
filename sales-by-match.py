from collections import Counter
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
count = Counter(ar)
print  (sum(value//2 for value in count.values()))