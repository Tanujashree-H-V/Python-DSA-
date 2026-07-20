class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if current number is too large
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # Move to next index (cannot reuse the same element)
                backtrack(i + 1, current, remaining - candidates[i])

                current.pop()

        backtrack(0, [], target)
        return result

candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))

candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates, target))