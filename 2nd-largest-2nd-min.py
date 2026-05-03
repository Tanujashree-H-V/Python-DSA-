ar=[1,2,3,7,4,5,6]
def secondLargest(ar):
    largest,secondLargest=float('-inf'),float('-inf')
    for num in ar:
        if num>largest:
            largest=num
        elif num<largest and num>secondLargest:
            secondLargest=num
    return secondLargest

def secondMin(ar):
    minimum,secondMin=float('inf'),float('inf')
    for num in ar:
        if num<minimum:
            minimum=num
        elif num>minimum and num<secondMin:
            secondMin=num
    return secondMin
print(secondLargest(ar))
print(secondMin(ar))