from collections import Counter
ar=[1,2,3,4,3,3,2,5]
count=Counter(ar)
min_freq=min(count.values())
max_freq=max(count.values())
print(min_freq)
print(max_freq)