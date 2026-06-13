from typing import List

class Solution:
    def intervalIntersection(self,firstList: List[List[int]],secondList: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0
        output = []

        while i < len(firstList) and j < len(secondList):

            # Find overlap
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If overlap exists
            if start <= end:
                output.append([start, end])

            # Move the interval that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return output


sol = Solution()

print(
    sol.intervalIntersection(
        [[0,2],[5,10],[13,23],[24,25]],
        [[1,5],[8,12],[15,24],[25,26]]
    )
)