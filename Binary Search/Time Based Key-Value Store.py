"""
Solution 1:
Binary Search

Time Complexity: O(n) for set, O(logn) for get
Space complexity : O(n)


Problem: TLE.  

Because this line:
self.value_map[key] = self.value_map.get(key, []) + [(timestamp, value)], this operation is actually O(n),
where n is the number of elements in the list. In python, `+` operand on list will create a new arrary,
which includes copying all elements to a new place
"""


class TimeMap:

    def __init__(self):
        self.value_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_map[key] = self.value_map.get(
            key, []) + [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.value_map:
            return ""

        value_list = self.value_map.get(key)
        if timestamp < value_list[0][0]:
            return ""

        if timestamp >= value_list[-1][0]:
            return value_list[-1][1]

        start, end = 0, len(value_list) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if value_list[mid][0] <= timestamp:
                start = mid
            elif value_list[mid][0] == timestamp:
                return value_list[mid][1]
            else:
                end = mid

        return value_list[start][1]


"""
Solution 1:
Binary Search

Time Complexity: O(logn)
Space complexity : O(n)
"""


class TimeMap:

    def __init__(self):
        self.value_map = {}
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.value_map:
            self.value_map[key] = []

        self.value_map[key].extend([(timestamp, value)])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.value_map:
            return ""

        value_list = self.value_map.get(key)
        if timestamp < value_list[0][0]:
            return ""

        if timestamp >= value_list[-1][0]:
            return value_list[-1][1]

        start, end = 0, len(value_list) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if value_list[mid][0] <= timestamp:
                start = mid
            else:
                end = mid

        return value_list[start][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
