class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand(left: int, right: int) -> None:
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Update longest palindrome found
            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1

        for i in range(len(s)):
            # Odd-length palindrome
            expand(i, i)
            # Even-length palindrome
            expand(i, i + 1)

        return s[start:end + 1]

sol = Solution()
print(sol.longestPalindrome("babad"))  
print(sol.longestPalindrome("cbbd")) 