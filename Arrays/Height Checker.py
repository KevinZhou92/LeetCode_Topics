"""
Solution 1:

Sort and loop through array

Time Complexity: O(nlogn)
Space complexity : O(1)
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        diff = 0
        for index in range(len(heights)):
            if heights[index] != expected[index]:
                diff += 1
                
        return diff
        
