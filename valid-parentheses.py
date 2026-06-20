class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in pairs:
                # ch is a closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # ch is an opening bracket
                stack.append(ch)

        return not stack
    

sol = Solution()

print(sol.isValid("()"))      # True
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))      # False
print(sol.isValid("([])"))    # True
print(sol.isValid("([)]"))    # False