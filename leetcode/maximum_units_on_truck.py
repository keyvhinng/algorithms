from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        
        for numberOfBoxes, numberOfUnitPerBox in boxTypes:
            if numberOfBoxes  <= truckSize:
                truckSize -= numberOfBoxes
                ans += numberOfBoxes * numberOfUnitPerBox
            else:
                ans += truckSize * numberOfUnitPerBox
                break

            
        return ans
