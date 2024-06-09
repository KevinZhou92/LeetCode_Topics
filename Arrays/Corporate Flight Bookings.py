"""
Solution 1:

Build a diff array, then we could use just O(n) time to construct the result array.
Difference array is really useful if we have to frequently change the value for all elements in a range.

Time Complexity: O(n) where k is the number of updates and n is the length of resulting array
Space complexity : O(n), can be O(1) since here we are just starting with an all-zero array
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        if not bookings or n <= 0:
            return [0]

        seats = [0 for _ in range(n)]
        for booking in bookings:
            start, end, add_seat = booking
            seats[start -  1] += add_seat
            if end < n:
                seats[end] -= add_seat
        
        for i in range(1, n):
            seats[i] = seats[i - 1] + seats[i]
        
        return seats