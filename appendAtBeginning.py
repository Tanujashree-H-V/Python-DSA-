from collections import deque

li = deque([1, 3, 4, 5, 7])
li.appendleft(6)
print(list(li))