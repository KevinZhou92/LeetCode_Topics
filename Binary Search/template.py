def binary_search(self, nums, target):
    # Corner Case
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            return mid
        else: 
            end = mid

    if nums[start] == target:
        return start
    
    if nums[end ] == target:
        return end
    
    return -1