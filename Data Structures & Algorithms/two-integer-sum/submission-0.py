class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index, value in enumerate(nums):
            if target-value in mp.keys():
                return [mp[target-value], index]
            mp[value] = index
        return [-1, -1]