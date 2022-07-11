"""
Solution 1:

Divide and Conqurer. 

Similar to how we solve merge sort

!!!Very tricky!!! Need to revisit.

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(buildings)
        if n == 0:
            return res

        if n == 1:
            start, end, height = buildings[0]
            return [[start, height], [end, 0]]

        leftSkyline = self.getSkyline(buildings[: n // 2])
        rightSkyline = self.getSkyline(buildings[n // 2:])

        return self.merge(leftSkyline, rightSkyline)

    def merge(self, leftSkylines, rightSkylines):
        leftHeight = rightHeight = curHeight = 0
        res = []
        leftIndex = rightIndex = 0
        leftEnd, rightEnd = len(leftSkylines), len(rightSkylines)

        while leftIndex < leftEnd and rightIndex < rightEnd:
            leftPoint, rightPoint = leftSkylines[leftIndex], rightSkylines[rightIndex]
            if leftPoint[0] < rightPoint[0]:
                index, leftHeight = leftPoint
                leftIndex += 1
            else:
                index, rightHeight = rightPoint
                rightIndex += 1

            maxHeight = max(leftHeight, rightHeight)
            if curHeight != maxHeight:
                self.update(index, maxHeight, res)
                curHeight = maxHeight

        self.appendSkylines(leftSkylines, leftIndex, leftEnd, curHeight, res)
        self.appendSkylines(rightSkylines, rightIndex,
                            rightEnd, curHeight, res)

        return res

    def appendSkylines(self, skylines, start, end, curHeight, res):
        while start < end:
            point = skylines[start]
            index, height = point
            start += 1
            if height != curHeight:
                self.update(index, height, res)
                curHeight = height

    def update(self, index, height, res):
        """
        Update the final output with the new element.
        """
        # if skyline change is not vertical -
        # add the new point
        if not res or res[-1][0] != index:
            res.append([index, height])
        # if skyline change is vertical -
        # update the last point
        else:
            res[-1][1] = height
