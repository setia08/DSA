from aiohttp_retry import List

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        zero=0
        one=0
        two=0

        for i in nums:
            if  i==0:
                zero+=1
            elif i==1:
                one+=1
            elif i==2:
                two+=1

        print([0]*zero + [1]*one + [2]*two)
        return [0]*zero + [1]*one + [2]*two
    

sol=Solution()
sol.sortColors([0])