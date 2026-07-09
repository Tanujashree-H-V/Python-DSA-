class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Current characters match?
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )

            # Next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = dp(i, j + 2) or (
                    first_match and dp(i + 1, j)
                )
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
    
s = "aa"
p = "a"

print(Solution().isMatch(s, p))

s = "aa"
p = "a*"

print(Solution().isMatch(s, p))

s = "ab"
p = ".*"

print(Solution().isMatch(s, p))