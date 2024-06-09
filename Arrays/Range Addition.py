"""
Solution 1:

Build a diff array, where each value in the array represent the delta between the corresponding element and the previous element in the original array


Time Complexity: O(n + k) where k is the number of updates and n is the length of resulting array
Space complexity : O(1), can be O(1) since here we are just starting with an all-zero array.
If we have an existing array with non-zero values, then we either:
1. Need extra space for storing the diffs
2. Or we could preprocess the existing array to make it an diff array before starting
"""
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        if not updates or len(updates) == 0:
            return [0 for _ in range(length)]
        
        diff_array = DiffArray(length)
        for update in updates:
            diff_array.update(update[0], update[1], update[2])
            
        
        return diff_array.build_array()

class DiffArray:
    def __init__(self, length):
        self.diff_array = [0 for _ in range(length)]

    def update(self, start, end, delta_val):
        self.diff_array[start] += delta_val
        if end + 1 < len(self.diff_array):
            self.diff_array[end + 1] -= delta_val

    def build_array(self):
        print(self.diff_array)
        new_array = [0 for _ in range(len(self.diff_array))]
        for idx in range(len(self.diff_array)):
            if idx == 0:
                new_array[idx] = self.diff_array[idx]
            else:
                new_array[idx] = new_array[idx - 1] + self.diff_array[idx]
        
        return new_array

        return 