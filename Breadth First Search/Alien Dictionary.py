"""
Solution 1:
BFS(https://leetcode.com/problems/alien-dictionary/solution/)

The key here is the order of two words are determined by the first different letter in two words

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        
        indegree = {c: 0 for word in words for c in word }
        # record letter that is greater than the current one
        neighbors = {char: set() for char in indegree}
        
        for index in range(len(words) - 1):
            cur, next = words[index], words[index + 1]
            for pos in range(min(len(cur), len(next))):
                cur_char, next_char = cur[pos], next[pos]
                if cur_char != next_char:
                    if next_char not in neighbors[cur_char]:
                        neighbors[cur_char].add(next_char)
                        indegree[next_char] += 1
                    break
                else:
                    # This line is really important for detecting invalid case
                    # for example, ['abc', 'ab'] is an invalid order because ab should show up before abc
                    if pos == min(len(cur), len(next)) - 1 and len(cur) > len(next):
                        return ""
                    
        
        queue = deque([c for c in indegree if indegree[c] == 0])
        
        res = []
        while len(queue) > 0:
            cur = queue.popleft()
            res.append(cur)
            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)
        
                
