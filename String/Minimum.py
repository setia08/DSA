from typing import List
class Solution:
    def minimumAbsoluteDifference(self, nums: List[int]) -> List[int]:
        nums.sort()
        min_gap=max(nums)
        new=[min_gap]

        for i in range(len(nums)-1):
            gap=nums[i+1]-nums[i]
            # print(gap)
            if gap<min_gap:
                min_gap=gap
                new[0]=[nums[i],nums[i+1]]
            elif gap==min_gap:
                new.append([nums[i],nums[i+1]])


        print(new)

Sol=Solution()

Sol.minimumAbsoluteDifference([4,5 ,10, 1, 3])
Sol.minimumAbsoluteDifference([1,3,6,10,15])
Sol.minimumAbsoluteDifference([3,8,-10,23,19,-4,-14,27])
