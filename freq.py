ar=[10,5,10,15,10,5]
s=[]
def freqNumber(ar):
    count=0
    for num in ar:
        if num in s:
            count+=1
        s.append(num)
    return count
print(freqNumber(ar))