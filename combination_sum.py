class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, current, remaining):
            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            # Explore candidates
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                current.append(candidates[i])

                # Reuse the same candidate
                backtrack(i, current, remaining - candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, [], target)
        return result
    
#example 1
candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))

#example 2
candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates, target))

#example 3
candidates = [2]
target = 1
print(Solution().combinationSum(candidates, target))