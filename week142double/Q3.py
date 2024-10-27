from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if i == k:
                return 0
            res1 = dfs(i + 1, j) + stayScore[i][j]
            res2 = max(dfs(i + 1, d) + s for d, s in enumerate(travelScore[j]))
            return max(res1, res2)
        return max(dfs(0, j) for j in range(n))

solution = Solution()
n=2
k=1
stayScore = [[2,3]]
travelScore = [[0,2],[1,0]]
print(solution.maxScore(n,k,stayScore,travelScore))