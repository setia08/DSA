from typing import List

class Solution:
    def fruitsIntoBaskets(self, nums: List[int]) -> List[int]:
        nums.reverse()
        output=[]
        counter=1
        for i in range(len(nums)):
            for j in range(i,len(output)):
                if nums[i] not  in output and counter<=2:
                    output.append(nums[i])
                    counter+=1
                elif nums[i] in output:
                    output.append(i)

                else:
                    continue
            return len(output)

from typing import List

class Solution:
    def fruitsIntoBaskets(self, fruits: List[int]) -> int:
        max_fruits = 0

        for left in range(len(fruits)):       # try every starting point
            basket = set()
            count = 0

            for right in range(left, len(fruits)):   # extend right
                basket.add(fruits[right])

                if len(basket) > 2:           # 3rd type found → stop
                    break

                count += 1

            max_fruits = max(max_fruits, count)

        return max_fruits

sol = Solution()
print(sol.fruitsIntoBaskets([1,2,1]))      # 3
print(sol.fruitsIntoBaskets([0,1,2,2]))    # 3
print(sol.fruitsIntoBaskets([1,2,3,2,2]))  # 4

