from itertools import chain
a=[1,2,3,4]
b=[5,6,7]
a.extend(chain(b))
print(a)