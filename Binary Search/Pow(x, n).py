"""
Solution 1:
Brute-force approach.

Time Complexity: O(n)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        res = x
        for i in range(abs(n) - 1):
            res *= x
        
        return res if n > 0 else 1 / res
        
        
        
        