from typing import List

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            g[p].append(i)


        dfsStr = [''] * n
        nodes = [[0, 0] for _ in range(n)]
        time = 0

        def dfs(x: int) -> None:
            nonlocal time
            nodes[x][0] = time
            for y in g[x]:
                dfs(y)
            dfsStr[time] = s[x]
            time += 1
            nodes[x][1] = time
        dfs(0)

        t = '#'.join(['^'] + dfsStr + ['$'])

        halfLen = [0] * (len(t) - 2)
        halfLen[1] = 1
        boxM = boxR = 0
        for i in range(2, len(halfLen)):
            hl = 1
            if i < boxR:
                hl = min(halfLen[boxM * 2 - i], boxR - i)
            while t[i - hl] == t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            halfLen[i] = hl


        def isPalindrome(l: int, r: int) -> bool:
            return halfLen[l + r + 1] > r - l

        return [isPalindrome(l, r) for l, r in nodes]

solution = Solution()
parent = [-1,0,0,1,1,2]
s = "aababa"
print(solution.findAnswer(parent,s))
print('----------------------------')
parent1 = [-1,0,0,0,0]
s1 = "aabcd"
print(solution.findAnswer(parent1,s1))