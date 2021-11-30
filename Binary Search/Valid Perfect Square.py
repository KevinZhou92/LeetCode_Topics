"""
Solution 1:
Binary Search

Time Complexity: O(logn)
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid < num:
                start = mid
            elif mid * mid == num:
                return True
            else:
                end = mid
                
        if start * start == num or end * end == num:
            return True
        
        return False
        