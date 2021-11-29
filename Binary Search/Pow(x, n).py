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

"""
Solution 2:
Divide and Conquer

Time Complexity: O(log  n)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        val = self.myPow(x, abs(n) // 2) 
        res = val * val
        if n % 2 == 1:
            res *= x
        
        return res if n > 0 else 1 / res
        
        
        
        
        
        
        
        