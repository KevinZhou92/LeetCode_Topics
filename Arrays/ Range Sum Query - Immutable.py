"""
Solution 1:

Build a prefix array so we can get sum of range efficiently


Time Complexity: O(n)
Space complexity : O(1)
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = self.build_prefix_sum(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        
    def build_prefix_sum(self, nums):
        prefix_sum = [0] * (len(nums) + 1)
        for idx in range(len(nums)):
            prefix_sum[idx + 1] = prefix_sum[idx] + nums[idx]
            
        return prefix_sum 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)