"""
Solution 1:
DFS + Memorization

Note: The input is not sorted!!!

Time Complexity: O(n^2)
Space complexity : O()
"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not profit:
            return 0

        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(
            len(profit))], key=lambda pair: pair[0])

        return self.search(jobs, -1, {})

    def search(self, jobs, lastIndex, mems):
        if lastIndex in mems:
            return mems[lastIndex]

        res = 0
        for index in range(lastIndex + 1, len(jobs)):
            if lastIndex != -1 and jobs[lastIndex][1] > jobs[index][0]:
                continue
            res = max(
                res, jobs[index][2] + self.search(jobs, index, mems))
        mems[lastIndex] = res

        return res

"""
Solution 2:
DFS + Binary Seach + Memorization

!!! Build a sorted array so we can binary search in it, which can reduce the complexity from n to logn

Time Complexity: O(nlogn)
Space complexity : O()
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not profit:
            return 0

        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(
            len(profit))], key=lambda pair: pair[0])

        return self.search(jobs, -1, {})

    def search(self, jobs, currentIndex, mems):
        if currentIndex in mems:
            return mems[currentIndex]
        
        if currentIndex == len(jobs):
            return 0

        nextIndex = self.find_next_job_index(jobs, currentIndex)
        mems[currentIndex] = max(jobs[currentIndex][2] + self.search(jobs, nextIndex, mems), self.search(jobs, currentIndex + 1, mems))

        return mems[currentIndex]
    
    def find_next_job_index(self, jobs, currentIndex):
        current_job = jobs[currentIndex]
        start, end = 0, len(jobs) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if jobs[mid][0] >= current_job[1]:
                end = mid
            else: 
                start = mid
        
        if jobs[start][0] >= current_job[1]:
            return start
        
        if jobs[end][0] >= current_job[1]:
            return end
        
        return len(jobs)
