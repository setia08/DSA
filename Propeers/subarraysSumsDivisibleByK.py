from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = 0

        for i in range(len(nums)):          # FIX 1: include all indices
            current_sum = 0
            for j in range(i, len(nums)):   # FIX 2: j starts at i, not i+1
                current_sum += nums[j]      # FIX 3: simple running sum, no prefix array
                if current_sum % k == 0:    # FIX 4: % not //
                    counter += 1

        return counter

sol = Solution()
print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))  # Output: 7
