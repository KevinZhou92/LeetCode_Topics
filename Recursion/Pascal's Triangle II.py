"""
Solution 1:

Iterative

Time Complexity: O(n^2)
Space complexity : O(n^2)

Saving only the last row could reduce space complexity to O(n)
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        rows = [[1], [1, 1]]
        for index in range(2, rowIndex + 1):
            res = []
            for i in range(index + 1):
                if i == 0:
                    res.append(1)
                elif i == index:
                    res.append(1)
                else:
                    res.append(rows[index - 1][i] + rows[index - 1][i - 1])
            rows.append(res)

        return rows[-1]


"""
Solution 2:

Recursion

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        prevRow = self.getRow(rowIndex - 1)
        cur = []
        for index in range(len(prevRow) + 1):
            if index == 0 or index == len(prevRow):
                cur.append(1)
            else:
                cur.append(prevRow[index - 1] + prevRow[index])

        return cur
