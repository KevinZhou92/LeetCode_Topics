"""
Solution 1:
Binary Search

Time Complexity: O(log(n)) for getHits
Space complexity : O(n)

Be carefule with edge case, for example, what happens to binary search if array is empty
"""


class HitCounter:

    def __init__(self):
        self.hit_timestamps = []

    def hit(self, timestamp: int) -> None:
        self.hit_timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if not self.hit_timestamps:
            return 0

        target = timestamp - 299
        start, end = 0, len(self.hit_timestamps) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hit_timestamps[mid] >= target:
                end = mid
            else:
                start = mid

        if self.hit_timestamps[start] >= target:
            return len(self.hit_timestamps) - start

        if self.hit_timestamps[end] >= target:
            return len(self.hit_timestamps) - end

        return 0


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


"""
Solution 2: 
Use a deque
https://www.cnblogs.com/grandyang/p/5605552.html

Time Complexity: O(n) worst case for getHits
Space complexity : O()
"""


class HitCounter:

    def __init__(self):
        self.hit_timestamps = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if not self.hit_timestamps:
            return 0

        while len(self.hit_timestamps) > 0:
            if self.hit_timestamps[0] <= timestamp - 300:
                self.hit_timestamps.popleft()
            else:
                break

        return len(self.hit_timestamps)


"""
Solution 3:
Use two rolling arrays for timestamps and hit on each timestamp.

Since we are only count for the past 300s from the current timestamp and the timestamps are increasing chronically.
We can keep a rolling array of size 300 for all the timestamps and a rolling array of size 300 for hit on each timestamp.

For each timestamp, we will take the mod against 300, if two timestamp fall in same location of the array, which means:
1. They are the same
2. Or 1 is 300 greater than the other one.

For Case 1, we just increment the hit count in another array
For Case 2, we will update the timestamp array with the greater timestamp and 
reset the hit count array to be 1 for the timestamp


Time Complexity: O(1)
Space complexity : O(1)
"""


class HitCounter:

    def __init__(self):
        self.timestamps = [False] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        if self.timestamps[timestamp % 300] == timestamp:
            self.hits[timestamp % 300] += 1
        else:
            self.timestamps[timestamp % 300] = timestamp
            self.hits[timestamp % 300] = 1

    def getHits(self, timestamp: int) -> int:
        if not self.timestamps:
            return 0

        count = 0
        for i in range(300):
            if self.timestamps[i] != False and self.timestamps[i] > timestamp - 300:
                count += self.hits[i]

        return count
