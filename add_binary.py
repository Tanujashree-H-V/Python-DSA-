class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()

print(s.addBinary("11", "1"))      # "100"
print(s.addBinary("1010", "1011")) # "10101"
print(s.addBinary("0", "0"))       # "0"
print(s.addBinary("111", "1"))     # "1000"