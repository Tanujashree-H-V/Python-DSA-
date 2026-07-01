class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         # Remove trailing spaces
        s = s.rstrip()
        
        # Find last space and compute length
        return len(s) - s.rfind(' ') - 1
    
length_of_last_word = Solution()
print(length_of_last_word.lengthOfLastWord("Hello World")) # Output: 5
print(length_of_last_word.lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
print(length_of_last_word.lengthOfLastWord("luffy is still joyboy")) # Output: 6