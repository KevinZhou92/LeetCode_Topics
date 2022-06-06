"""
Solution 1:

DFS
https://leetcode.com/problems/robot-room-cleaner/
https://www.cnblogs.com/grandyang/p/9988250.html
http://www.noteanddata.com/leetcode-489-Robot-Room-Cleaner-java-solution-note.html

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        self.search((0, 0), visited, 0, robot)

    def search(self, startPos, visited, dIndex, robot):
        visited.add(startPos)
        robot.clean()

        for index in range(4):
            x, y = startPos
            newIndex = (index + dIndex) % 4
            nextPos = (x + self.directions[newIndex]
                       [0], y + self.directions[newIndex][1])
            if nextPos not in visited and robot.move():
                self.search(nextPos, visited, newIndex, robot)
                self.goBack(robot)
            robot.turnRight()

    def goBack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
