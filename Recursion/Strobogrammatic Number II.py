"""
Solution 1:

Recursion

Generate all possible combinations from reversible numbers and check each of them to 
find the Strobogrammatic numbers.

Time Complexity: O(5^n * n)
Space complexity : O(5^n * n)
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Build a n digit number, make sure it's strobogrammatic
        # loop over 0-9 each time
        mirrorDigits = {
            0: 0,
            1: 1,
            6: 9,
            9: 6,
            8: 8,
        }

        res = []
        if n == 0:
            return res

        if n == 1:
            return ["0", "1", "8"]

        self.findStrobogrammaticNumber(0, n, 0, res, mirrorDigits)

        return res

    def findStrobogrammaticNumber(self, index, length, cur, res, mirrorDigits):
        if index == length:
            if self.checkStrobogrammatic(cur, mirrorDigits):
                res.append(str(cur))
            return

        for num in [0, 1, 6, 8, 9]:
            if index == 0 and num == 0 or num not in mirrorDigits:
                continue
            self.findStrobogrammaticNumber(
                index + 1, length, cur * 10 + num, res, mirrorDigits)

    def checkStrobogrammatic(self, number, mirrorDigits):
        newNumber = 0
        originalNumber = number
        while number != 0:
            newNumber = newNumber * 10 + mirrorDigits[number % 10]
            number //= 10

        return newNumber == originalNumber


"""
Solution 1-2:

Recursion

Instead of generating all possible combinations from reversible numbers, we can generate Strobogrammatic numbers
from some base cases(n = 0 and n = 1), we can generate longer Strobogrammatic numbers by appending reversible numbers
at the begining and in the end. The only corner case would be when to add 0, only if we are not appending the last two 
numbers, we can append 0 in the end and at the beginning.

For example, if n = 4, we already have ["11", "88", "69", "96", "00"], we cannot prepend and append 0 

Time Complexity: O(5^(n/2) * n)
Space complexity : O(5^(n/2) * n)
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Build a n digit number, make sure it's strobogrammatic
        # loop over 0-9 each time
        mirrorDigits = {
            0: 0,
            1: 1,
            6: 9,
            9: 6,
            8: 8,
        }

        return self.findStrobogrammaticNumber(n, n, mirrorDigits)

    def findStrobogrammaticNumber(self, length, totalLength, mirrorDigits):
        if length == 0:
            return [""]

        if length == 1:
            return ["0", "1", "8"]

        res = []
        for prevStro in self.findStrobogrammaticNumber(length - 2, totalLength, mirrorDigits):
            for num in mirrorDigits:
                if num == 0 and length == totalLength:
                    continue
                res.append(str(num) + prevStro + str(mirrorDigits[num]))

        return res


"""
Solution 2:

BFS
Level Order Traversal
Building numbers from shorter length
Need to pay attention on edge cases

https://leetcode.com/problems/strobogrammatic-number-ii/solution/

Time Complexity: O(N⋅5^N/2)
Space complexity : O(N⋅5^N/2)
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Build a n digit number, make sure it's strobogrammatic
        # loop over 0-9 each time
        mirrorDigits = { 
            0: 0,
            1: 1,
            6: 9,
            9: 6,
            8: 8,      
        }
        
        curLength = n % 2
        queue = deque(["0", "1", "8"]) if curLength == 1 else deque([""])
        while curLength < n:
            curLength += 2
            size = len(queue)
            for _ in range(size):
                curPair = queue.popleft()
                for num in mirrorDigits:
                    if num == 0 and curLength == n:
                        continue
                    queue.append(str(num) + curPair + str(mirrorDigits[num]))
        
        return queue
        