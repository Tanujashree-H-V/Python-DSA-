class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # index for valid elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
    
nums = [0,1,2,2,3,0,4,2]
val = 2
k = Solution().removeElement(nums, val)

print(k)        # 5
print(nums[:k]) # [0, 1, 3, 0, 4] (order may vary)