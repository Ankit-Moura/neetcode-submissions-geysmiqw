class Solution:
    def trap(self, height: List[int]) -> int:
# water[A->B] = max(min(A, B) * (index(B)-index(A)-1) - all Heights in between, 0)
        total = 0
        l = mr = ml = 0
        r = len(height)-1
    
        while(l<r):
            if(height[l]<=height[r]): 
                ml = max(ml, height[l])
                w = ml - height[l]
                if w>0:
                    total += w
                l+=1
            else:
                mr = max(mr, height[r])
                w = mr - height[r]
                if w>0:
                    total += w
                r-=1

        return total