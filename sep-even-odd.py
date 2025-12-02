l=[3,6,8,5,1,4,10]
def even_odd_sep(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd 
even,odd=even_odd_sep(l)
print(even)
print(odd)