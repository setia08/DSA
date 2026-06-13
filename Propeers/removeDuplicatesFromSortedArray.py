from typing import List

class Solution:
    def removeDuplicatesFromSortedArray(self, nums: List[int]) -> int:
        k = 1  # first element is always unique

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # found a new unique element
                nums[k] = nums[i]       # place it in the "clean" section
                k += 1

        return k


new_sol = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = new_sol.removeDuplicatesFromSortedArray(nums)
print(k, nums[:k])  # 5 [0, 1, 2, 3, 4]