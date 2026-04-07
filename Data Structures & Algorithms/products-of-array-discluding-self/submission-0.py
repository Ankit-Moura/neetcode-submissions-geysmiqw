class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        is_one_zero = z_index = is_two_zero = False
        total = 1
        for i in  range(len(nums)):
            if not nums[i]:
                if not is_one_zero:
                    is_one_zero = True
                    z_index = i 
                    continue
                else:
                    is_two_zero = True
                    break
            total *= nums[i]
        result = [0]*len(nums)
        if is_two_zero:
            return result
        
        
        if is_one_zero:
            result[z_index] = total
            return result

        # when there are no zeros in the nums
        for i in range(len(nums)):
            result[i] = int(total/nums[i])
        
        return result
        
                