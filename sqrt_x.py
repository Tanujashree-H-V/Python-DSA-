class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        r = x
        while r * r > x:
            r = (r + x // r) // 2

        return r
    

s = Solution()

print(s.mySqrt(4))   # 2
print(s.mySqrt(8))   # 2
print(s.mySqrt(0))   # 0
print(s.mySqrt(1))   # 1
print(s.mySqrt(16))  # 4
print(s.mySqrt(27))  # 5