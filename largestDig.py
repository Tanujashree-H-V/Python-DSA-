ar=[1,3,5,2,6,8,9]
def largestDig(ar):
    ans=float('inf')
    for i in range(len(ar)):
        if ar[i]<ans:
            ans=ar[i]
    return ans
print(largestDig(ar))
        