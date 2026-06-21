from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] = nums[i - 1] + nums[i]
            print(nums)
        prefix_sum_count = {0: 1}  
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return count

# Example usage
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1]
    k = 2
    print(sol.subarraySum(nums, k)) 
