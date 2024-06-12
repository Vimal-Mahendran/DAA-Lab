def removeElement(nums, val):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1
    
    return left

nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("Resulting array:", nums[:k])
print("k:", k) 