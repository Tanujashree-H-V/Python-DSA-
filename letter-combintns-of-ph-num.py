class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                res.append(path)
                return

            for ch in phone[digits[index]]:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return res

sol = Solution()

print(sol.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations("2")) # ["a","b","c"]