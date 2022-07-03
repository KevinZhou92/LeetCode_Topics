"""
Solution 1:

Recursion

This is deviated from LeetCode 77. LC77 only asks us for possible combinations, but this question
asks us to make each combination sum up to a target value, we just need to add this constraint
in the backtracking check and that is it.

Time Complexity: O()
Space complexity : O(n)
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.search(1, k, n, [], res)
        
        return res
    
    def search(self, startNum,  k, remain, cur, res):
        if len(cur) == k:
            if remain == 0:
                res.append(copy.copy(cur))     
            return
        
        for num in range(startNum, 10):
            if num > remain:
                continue
            cur.append(num)
            self.search(num + 1, k, remain - num, cur, res)
            cur.pop()
        