"""
Solution 1:
1. Find the element in the array that is closed to the target
2. Fan out from the closest element to the left and to the right, both for k step
3. Compare the distance of 2k - 1 element and find the k closet

Time Complexity: O(klogk + logn)
Space Complexity: O(k)

Note: Edge case, the comparator rule is customized, we need to be careful when compare elements with
the target
"""
from functools import cmp_to_key

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_index = self.get_closest_index(arr, x)
        candidates = [(arr[closest_index], x)]
        for index in range(1, k):
            if (closest_index - index) < 0:
                continue
            candidates.append((arr[closest_index - index], x))
        
        for index in range(1, k):
            if (closest_index + index) >= len(arr):
                continue
            candidates.append((arr[closest_index + index], x))
            
        candidates = sorted(candidates, key=cmp_to_key(self.comparator))[:k]
        
        res = []
        
        for can in candidates:
            res.append(can[0])
            
        return sorted(res)
    
    def get_closest_index(self, arr, target):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] > target:
                end = mid
            else:
                start = mid
                
        if abs(arr[start] - target) <= abs(arr[end] - target):
            return start
        
        return end
        
    def comparator(self, t1, t2):
        # num - target
        if abs(t1[0]- t1[1]) < abs(t2[0]- t2[1]):
            return -1
        if abs(t1[0]- t1[1]) == abs(t2[0]- t2[1]) and t1[0] < t2[0]:
            return -1
        
        return 1

"""
Solution 2: Two Pointer
1. Find the element in the array that is closed to the target and start with this element in the resulting array
2. Fan out from the closest element to the left and to the right using two pointers

Time Complexity: O(logn) + O(k)
Space Complexity: O(1)
"""
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_index = self.get_closest_index(arr, x)
        left, right = closest_index - 1, closest_index + 1
        res = [arr[closest_index]]
        while left >= 0 and right < len(arr) and len(res) < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        
        while left >= 0 and len(res) < k:
            res.append(arr[left])
            left -= 1
            
        while right < len(arr) and len(res) < k:
            res.append(arr[right])
            right += 1
            
        return sorted(res)
    
    def get_closest_index(self, arr, target):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] > target:
                end = mid
            else:
                start = mid
                
        if abs(arr[start] - target) <= abs(arr[end] - target):
            return start
        
        return end