"""
Solution 1:

Recursion

Time Complexity: O(k * n)
Space complexity : O(n)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''

        return self.decode(0, s)[0]

    def decode(self, index, s):
        # loop over the string
        # if it's a number, which mean we need to unfold the following sub string
        # it's a valid string we will start from [ until we met a correspoing ]
        res = ""
        count = 0
        while index < len(s):
            if s[index].isdigit():
                count = count * 10 + int(s[index])
            elif s[index].isalpha():
                res += s[index]
            elif s[index] == '[':
                subString, lastIndex = self.decode(index + 1, s)
                res += count * subString
                index = lastIndex
                count = 0
            else:
                return res, index
            index += 1

        return res, index


"""
Solution 2:

Use stack

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        if not s:
            return res

        # maintain a stack, it could be numbers or a substring
        # pop value in the stack whenever a ] is encountered
        stack = []
        # 3[a2[c]]
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curString = ""
                while stack and stack[-1] != "[":
                    curString = stack.pop() + curString
                # remove [
                stack.pop()
                count = 0
                base = 1
                while stack and stack[-1].isdigit():
                    count = int(stack.pop()) * base + count
                    base *= 10
                stack.append(count * curString)
                count = 0

        return ''.join(stack)
