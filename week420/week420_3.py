import math
from symbol import factor
from traceback import format_exc
from typing import List


class Solution:
    def minOperations(self,nums:List[int]) -> int:
        def find_factor(N):
            for i in range(2,int(math.sqrt(N))+1):
                if N % i == 0:
                    return i
            return N

        count = 0
        n = len(nums)
        prev = nums[-1]
        for i in range(n-2,-1,-1):
            if nums[i] <= prev:
                prev = nums[i]
                continue
            factor = find_factor(nums[i])
            if factor > prev:
                return -1
            count += 1
            prev = factor
        return count

solution = Solution()
nums1 = [25,7]
print(solution.minOperations(nums1))
nums2 = [7,7,6]
print(solution.minOperations(nums2))
nums3 = [1,1,1,1]
print(solution.minOperations(nums3))