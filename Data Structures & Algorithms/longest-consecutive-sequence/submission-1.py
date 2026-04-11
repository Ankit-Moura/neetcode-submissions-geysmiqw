class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hash_set = set(nums)
        mx_streak = start = 1
        for ele in hash_set:
            streak = 1
            if  ele-1 in hash_set:
                continue
            st = ele
            while 1:
                if st+1 in hash_set:
                    streak+=1
                    st += 1
                else:
                    break
            if mx_streak < streak:
                mx_streak = streak
                start = st-streak
            
        return mx_streak

        