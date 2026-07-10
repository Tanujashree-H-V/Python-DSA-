class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
    
nums = [3,2,2,3]
val = 3

sol = Solution()
k = sol.removeElement(nums, val)

print(k)
print(nums[:k])

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2

sol = Solution()
k = sol.removeElement(nums1, val1)

print(k)
print(nums1[:k])