class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack(current)

                current.pop()
                used[i] = False

        backtrack([])
        return result

nums = [1,2,3]
print(Solution().permute(nums))

nums = [0,1]
print(Solution().permute(nums))

nums = [1]
print(Solution().permute(nums))