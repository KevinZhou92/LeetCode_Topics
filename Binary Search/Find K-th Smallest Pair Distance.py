"""
Solution 1:
Brute-Force
Generate All possible results and find kth smallest distance

Time Complexity: O(n^2), where m and n are lengths of two lists
Space complexity : O(n^2) 
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        distances = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                distances.append(abs(nums[i] - nums[j]))
        distances.sort()
        return distances[k - 1]                       
                       
                
                       
        
        