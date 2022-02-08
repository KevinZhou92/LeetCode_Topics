"""
Solution 1:
Binary Search

Time Complexity: O(nlogn)
Space complexity : O(1)
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if not weights:
            return -1

        accum_weights = []
        for index in range(len(weights)):
            if not accum_weights:
                accum_weights.append(weights[index])
            else:
                accum_weights.append(accum_weights[index - 1] + weights[index])

        start_capacity, end_capacity = 0, sum(weights)
        while start_capacity + 1 < end_capacity:
            capacity = start_capacity + (end_capacity - start_capacity) // 2
            if self.possible(weights, capacity, days):
                end_capacity = capacity
            else:
                start_capacity = capacity

        if self.possible(weights, start_capacity, days):
            return start_capacity

        if self.possible(weights, end_capacity, days):
            return end_capacity

        return -1

    def possible(self, weights, capacity, days):
        res = 1
        count = 0
        for weight in weights:
            if count + weight <= capacity:
                count += weight
            else:
                count = weight
                res += 1

            if weight > capacity:
                return False

        return res <= days
