from typing import List
class Solution:
    def insertInterval(self, nums: List[int], out:List[int]):
        print(nums,out)
        outer=[nums[0]]
        for i in range(len(nums)):
            if max(nums[i])>min(out) and max(out)>min(nums[i]):
                new_arr=[min(nums[i]),max(out)]
                outer.append(new_arr)
                print(new_arr)
            else:
                print("nums",nums[i])
                outer.append(nums[i])
        print(outer)


Sol=Solution()
Sol.insertInterval([[1,3],[6,9]], [2,5])  # [[1,5],[6,9]]