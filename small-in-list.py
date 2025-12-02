x=int(input("enter the value for x: "))
l=[2,3,76,45,23,54]
def smallElement_in_list(l,x):
    res=[]
    for i in l:
        if i <x:
            res.append(i)
    return res

print(smallElement_in_list(l,x))