"""
Solution 1:

Recursion
We need to classify possible scenarios.
1. Base case: we used all remainig left and right parentheses, in this case, we will add the result and return
2. We used all the left parentheses, in this case, we can only keep adding right parentheses
3. There are both remaining left and right parentheses and there are more right parentheses, we can either add a left parenthese
or add a right parentheses here
4. There same number of remaining left and right parentheses, we can only add left parenthese in this case
otherwise it's an invalid pair
Time Complexity: O(2^n)
Space complexity : O(2^n) Use space to store the result
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we will enumerate possible left or right parenthese on each position
        self.res = []
        self.search(n, n, n, "")

        return self.res

    def search(self, n, leftRemains, rightRemains, currentComb):
        # case 1
        if leftRemains == 0 and rightRemains == 0:
            self.res.append(currentComb)
            return

        # case 2
        if leftRemains == 0:
            self.search(n, leftRemains, rightRemains - 1, currentComb + ")")

        # case 3
        if leftRemains != 0 and leftRemains < rightRemains:
            self.search(n, leftRemains - 1, rightRemains, currentComb + "(")
            self.search(n, leftRemains, rightRemains - 1, currentComb + ")")

        if leftRemains == rightRemains:
            self.search(n, leftRemains - 1, rightRemains, currentComb + "(")


"""
Solution 1-2:

Concise version

https://leetcode.com/problems/generate-parentheses/solution/
Time Complexity: O() Catlan Number
Space complexity : O() Catlan Number
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we will enumerate possible left or right parenthese on each position
        res = []
        self.search(n, 0, 0, "", res)

        return res

    def search(self, n, leftCount, rightCount, curPath, res):
        if leftCount == n and rightCount == n:
            res.append(curPath)
            return

        if leftCount > rightCount:
            self.search(n, leftCount, rightCount + 1, curPath + ")", res)

        if leftCount < n:
            self.search(n, leftCount + 1, rightCount, curPath + "(", res)
