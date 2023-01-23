"""
Solution 1:

Start from the end of the arrary, make sure that we loop through everything in the array

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # loop the array in a reverse order, we will ensure that
        # we know what's the max element to the right of current element
        if not arr:
            return arr
        
        index = len(arr) - 1
        maxEle = arr[-1]
        arr[index] = -1
        index -= 1
        while index >= 0:
            nextMax = max(arr[index], maxEle)
            arr[index] = maxEle
            maxEle = nextMax
            index -= 1
        
        return arr
        
    