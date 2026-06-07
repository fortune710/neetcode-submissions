from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        keys = [i for i in range(1, n + 1)]
        outdegree = dict.fromkeys(keys, 0)
        indegree = dict.fromkeys(keys, 0)


        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for key in keys:
            if outdegree[key] == 0 and indegree[key] == n- 1:
                return key
        
        return -1