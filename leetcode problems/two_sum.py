from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp: List[int] = []
        for item in range(len(nums)):
            for j in range(item+1 , len(nums)):
                if item == j:
                    break
                elif nums[item] + nums[j] == target:
                    temp.append(item)
                    temp.append(j)
                    return temp

        return nums


print(Solution().two_sum([1, 2, 3], 5))
