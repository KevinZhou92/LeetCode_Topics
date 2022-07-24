"""
Solution 1:

Recursion

Divide and conquer

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression:
            return []
        
        res =[]
        inputString = ''
        for index in range(len(expression)):
            curChar = expression[index]
            if curChar in '+-*':
                leftRes = self.diffWaysToCompute(expression[:index])
                rightRes = self.diffWaysToCompute(expression[index + 1:])
                for lRes in leftRes:
                    for rRes in rightRes:
                        if curChar == '+':
                            res.append(lRes + rRes)
                        elif curChar == '-':
                            res.append(lRes - rRes)
                        else:
                            res.append(lRes * rRes)
        
        if res == []:
            return [int(expression)]
        
        return res
        