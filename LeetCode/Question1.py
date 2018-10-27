def twosum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums[i + 1:]:
            return [i, nums.index(target - nums[i], i + 1)]


a = [3, 2, 4]
print(twosum(a, 6))
