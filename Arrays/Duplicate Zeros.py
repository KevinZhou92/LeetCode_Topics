"""
Solution 1:

Two Pointer

If we duplicate all zeros in the array, we would need a new array that is big enough to hold all duplicated zeros.
Then the problem becomes how we can make the new array small enough so that it can fit in the original array, we
can start removing elements from the tail of both arrays, we would need to remove two elements from the new arrary
if the current tail element from original array is a zero.

We need to pay attention to an edge case, if the tail zero from the original arrary is not duplicated due to space restriction,
then we should just move the zero from the original arrayr and move a corresponding element from the new arrary(instead of two in other cases)

This is a tricky question, we need to think about how can we make the change without additional space and sometimes start from the tail
is a good option.

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr) == 0:
            return
        
        countOfZeros = sum(1 for num in arr if num == 0)
        leftIndex = len(arr) -1
        rightIndex = len(arr) + countOfZeros - 1
        
        
        while leftIndex >= 0:
            if rightIndex > len(arr) - 1:
                if arr[leftIndex] == 0:
                    rightIndex -= 2
                else:
                    rightIndex -= 1
                leftIndex -= 1
                if rightIndex == len(arr) - 2:
                    arr[rightIndex + 1] = 0
            else:
                arr[rightIndex] = arr[leftIndex]
                if arr[leftIndex] == 0:
                    rightIndex -= 1
                    arr[rightIndex] = 0
                leftIndex -= 1
                rightIndex -= 1


"""
Optimized

"""            
class Solution2:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr) == 0:
            return
        
        countOfZeros = sum(1 for num in arr if num == 0)
        leftIndex = len(arr) -1
        rightIndex = len(arr) + countOfZeros - 1
        
        while leftIndex >= 0:
            if rightIndex > len(arr) - 1:
                if arr[leftIndex] == 0:
                    rightIndex -= 1
                leftIndex -= 1   
                rightIndex -= 1
                if rightIndex == len(arr) - 2:
                    arr[rightIndex + 1] = 0
            else:
                arr[rightIndex] = arr[leftIndex]
                if arr[leftIndex] == 0:
                    rightIndex -= 1
                    arr[rightIndex] = 0
                leftIndex -= 1
                rightIndex -= 1
                
        
        
                    
                    
        