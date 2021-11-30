"""
Solution 1:
Binary Search Approach.

Note: Special condition is 
Note that the letters wrap around.
For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        while start + 1 < end:
            mid = start + (end -start) // 2
            if ord(letters[mid]) > ord(target):
                end = mid
            else:
                start = mid
                
        if ord(letters[start]) > ord(target):
            return letters[start]
        
        if ord(letters[end]) <= ord(target):
            return letters[0]
        
        return letters[end]
        