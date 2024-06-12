def permuteUnique(nums):
    def backtrack(path, nums):
        if len(path) == len(nums):
            result.append(path)
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            backtrack(path + [nums[i]], nums)
            used[i] = False

    nums.sort()
    result = []
    used = [False] * len(nums)
    backtrack([], nums)
    return result

nums1 = [1, 1, 2]
print(permuteUnique(nums1))

nums2 = [1, 2, 3]
print(permuteUnique(nums2))