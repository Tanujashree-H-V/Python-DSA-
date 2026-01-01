nums=[2,7,4,11,15]
target=11
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print ([i, j])