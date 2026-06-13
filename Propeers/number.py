# argest Number
# Medium
# Acceptance: 29.8%
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Examples:
# Example 1:

# Input:
# [10,2]

# Output:
# "210"

# Explanation:
# By arranging 2 before 10, the largest number formed is 210.

# Example 2:

# Input:
# [3,30,34,5,9]

# Output:
# "9534330"

# Explanation:
# By arranging the numbers as 9, 5, 34, 3, 30, the largest number formed is 9534330.
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        number=""
        nums=[str(e) for e in nums]
        biggest=type(int)
        for i in nums:
            print(i)
            
            print("biggest:", biggest)
            if biggest<i[0]:
                print("Found a bigger number:", i)
                biggest=i
                number+=i
                print("number:", number)
                nums.remove(i)
                
        return number

Sol=Solution()
print(Sol.largestNumber([10,2]))