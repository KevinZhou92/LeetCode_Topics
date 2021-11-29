"""
Check Search in Rotated Sorted Array

The only difference is we don't know the size of the array, so 
we should use binary search to calculate for the size of the array first
then do a binary search to find the target
"""
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # calculate size
        size = self.get_array_size(reader)
        return self.binary_search(0, size, target, reader)
    
    def binary_search(self, start, end, target, arrayReader):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arrayReader.get(mid) > arrayReader.get(end):
                if arrayReader.get(start) <= target and arrayReader.get(mid) >= target:
                    end = mid
                else:
                    start = mid
            else:
                if arrayReader.get(mid) <= target and arrayReader.get(end) >= target:
                    start = mid
                else:
                    end = mid
        
        if arrayReader.get(start) == target:
            return start
        if arrayReader.get(end) == target:
            return end
        
        return -1
        
        
    def get_array_size(self, arrayReader):
        tmp = 1
        while arrayReader.get(tmp) != 2 ** 31 - 1:
            tmp *= 2
            
        start, end = tmp // 2, tmp
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arrayReader.get(mid) == 2 ** 31 - 1:
                end = mid
            else:
                start = mid
                
        if arrayReader.get(end) != 2 ** 31 - 1:
            return end
        
        return start
            
        