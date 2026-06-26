class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            curr_height = min(height[left], height[right])
            max_area = max(max_area, width * curr_height)

            # Move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))  # 49