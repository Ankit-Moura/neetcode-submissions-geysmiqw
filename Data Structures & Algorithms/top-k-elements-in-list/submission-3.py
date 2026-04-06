class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num in mp.keys():
                mp[num] += 1
            else:
                mp[num] = 1

        arr = [[] for _ in range(len(nums) + 1)]

        for key , v in mp.items():
            arr[v].append(key)
        
        result = []
        for i in range(len(arr) - 1, -1, -1):
            if k <= 0:
                break
            for num in arr[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    break
        return result
            
        
            
