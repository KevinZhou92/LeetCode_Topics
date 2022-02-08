"""
Solution 1:
HashMap + Binary Search

Initial Thought was to create a hashmap and store the copy of the array everytime we take snapshot, the problem of this approach
would be if we frequently do snapshot, the time complexity would be O(n)

Time Complexity: O(logn) for search, O(1) for all other ops
Space complexity : O()
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # snap_id, val
        self.arrays = {index: [[0, 0]] for index in range(length)}

    def set(self, index: int, val: int) -> None:
        self.arrays[index].append([self.snap_id, val])

    def snap(self) -> int:
        res = self.snap_id
        self.snap_id += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        return self.search(self.arrays[index], snap_id)

    def search(self, array, snap_id):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid][0] > snap_id:
                end = mid
            else:
                start = mid

        if array[end][0] <= snap_id:
            return array[end][1]

        return array[start][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
