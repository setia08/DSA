from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            fixed = nums[i]
            right_most = i + 1
            left_most = len(nums) - 1

            while right_most < left_most:
                current_sum = fixed + nums[right_most] + nums[left_most]

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                if current_sum == target:
                    return closest
                elif current_sum < target:
                    right_most += 1
                else:
                    left_most -= 1

        return closest

hello = Solution()
hello.threeSumClosest([0,0,0], 1)