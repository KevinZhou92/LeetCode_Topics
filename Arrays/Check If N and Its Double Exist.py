"""
Solution 1:

HashTable

Time Complexity: O(N)
Space complexity : O(N)
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr:
            return False
        
        targets = set()
        for num in arr:
            if num in targets:
                return True
            targets.add(num / 2)
            targets.add(num * 2)
            
        return False
        