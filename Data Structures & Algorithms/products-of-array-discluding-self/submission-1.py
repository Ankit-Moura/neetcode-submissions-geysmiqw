class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        # compute prod prefix
        pre = 1
        for i in range(1, len(nums)):
            pre *= nums[i-1]
            res.append(pre)
        suf = 1
        for i in range(len(nums)-2, -1, -1):
            suf *= nums[i+1]
            res[i] *= suf

        return res
                