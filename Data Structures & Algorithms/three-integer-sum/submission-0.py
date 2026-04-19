class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            target = 0-nums[i]
            
            st = i+1
            end = len(nums) - 1
            while(st<end):
                total = nums[st] + nums[end]
                if total == target:
                    if i!=st and st!=end and i!=end:
                        res.add((nums[i], nums[st], nums[end]))
                        st+=1
                        continue
                if total > target:
                    end -= 1
                else:
                    st+=1
        
        return [list(item) for item in res]
                