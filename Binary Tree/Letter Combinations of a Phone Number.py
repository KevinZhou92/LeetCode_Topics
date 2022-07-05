"""
Solution 1:

Backtracking

Time Complexity: O(4^n * n)
Space complexity : O(n)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res

        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.search(digits, 0, digitMap, [], res)

        return res

    def search(self, digits, index, digitMap, comb, res):
        if len(comb) == len(digits):
            res.append(''.join(comb))
            return

        for letter in digitMap[digits[index]]:
            comb.append(letter)
            self.search(digits, index + 1, digitMap, comb, res)
            comb.pop()
