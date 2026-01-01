nums1=[1,3]
nums2=[2]
ans=nums1+nums2
ans.sort()
n=len(ans)
if n % 2!=0:
    print(ans[n//2])
else:
    print((ans[n//2]+ans[(n//2)-1])/2)