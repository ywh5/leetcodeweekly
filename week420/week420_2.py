from collections import defaultdict
from email.policy import default


class Solution:
    def numberofSubstringS(self,s:str,k:int) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
            while cnt[c] >= k:
                cnt[s[left]] -= 1
                left += 1
            ans += left
        return ans
solution = Solution()
s = 'abacb'
k=2
print(solution.numberofSubstringS(s,k))
s1 = 'ababc'
k=1
print(solution.numberofSubstringS(s1,k))