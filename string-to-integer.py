class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Check overflow BEFORE it happens
            if result > INT_MAX // 10 or \
               (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
    

sol = Solution()

print(sol.myAtoi("42"))            
print(sol.myAtoi("   -042"))       
print(sol.myAtoi("1337c0d3"))      
print(sol.myAtoi("0-1"))           
print(sol.myAtoi("words and 987")) 