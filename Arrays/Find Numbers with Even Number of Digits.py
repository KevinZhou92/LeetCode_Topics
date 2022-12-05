"""
Solution 1:

Loop

Time Complexity: O(n * m) where m is the max lenghth of a word
Space complexity : O(1)
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digit_count = self.getCount(num)
            if digit_count % 2 == 0:
                count += 1
                
        return count
    
    def getCount(self, num):
        count = 0
        while num != 0:
            num //= 10
            count += 1
        
        return count