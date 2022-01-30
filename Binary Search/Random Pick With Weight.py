"""
https://leetcode-cn.com/problems/random-pick-with-weight/solution/tu-jie-an-quan-zhong-sui-ji-xuan-ze-zhi-pu1mv/
Additional Knowledge: https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/09.pdf
Solution 1:
Binary Search

This is a tricky problem. This is to select basedon each element's weight.
Assume we have an array [1, 9], then we should pick 9 nine times out of 10 picks and 1 only 1 time.

There is a built-in function random.randomint(start, end) than can generate a random number between
start and end(inclusively). But every number will be generated with an euqal probability.

We can't simply call random.randomint() and return the value.

To apply weight in the selection, we calculate the prefix sums of the array, then we can project the weight of
each number linearly. For example:

[3, 1, 4], the sum is 8, and there is 8 integers between [1, 8] which are 1,2,3,4,5,6,7,8
According to the weight of each number, if we pick 8 times, we should pick index 0 three times,
index 1 one time and index 2 four times. Combine this fact with our prefix sums. If the number generated are 1, 2, 3
then we pick index 0, if the number generated is 4, we pick index 1, if the number generated are 5,6,7,8, we will pick index 2
We can do this by searching the number in the random array.

Time Complexity: O(logn)
Space complexity: O(1) 


"""


class Solution:

    def __init__(self, w: List[int]):
        self.sums = sum(w)
        self.prefix_sums = []
        for num in w:
            if not self.prefix_sums:
                self.prefix_sums.append(num)
            else:
                self.prefix_sums.append(self.prefix_sums[-1] + num)

    def pickIndex(self) -> int:
        return self.search(self.prefix_sums, random.randint(1, self.sums))

    def search(self, prefix_sums, target):
        start, end = 0, len(prefix_sums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if prefix_sums[mid] >= target:
                end = mid
            else:
                start = mid

        if prefix_sums[start] >= target:
            return start

        return end


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

"""
Solution 1 - 1:
Binary Search
"""


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        return self.search(self.prefix_sums, random.random() * self.total_sum)

    def search(self, prefix_sums, target):
        start, end = 0, len(prefix_sums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if prefix_sums[mid] >= target:
                end = mid
            else:
                start = mid

        if prefix_sums[start] >= target:
            return start

        return end
