"""
Solution 1:

Loop the array

Be careful if the array is monolithic

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        index = 0
        while index < len(arr) - 1:
            if index != 0 and arr[index] > arr[index - 1] and arr[index] > arr[index + 1]:
                break
            if arr[index] >= arr[index + 1]:
                return False       
            index += 1
        
        if index == len(arr) - 1:
            return False
            
        while index < len(arr) - 1:
            if arr[index] <= arr[index + 1]:
                return False
            index += 1
            
        return True
            