a = [(1, 2), (), (3, 4), (), (5,)]
res=[]
#res = [t for t in a if t]       
for t in a:
    if t:
        res.append(t)
print(res)