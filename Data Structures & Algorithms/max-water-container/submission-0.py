class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        i = 0
        j = len(heights)-1
        while(i<j):
            l = min(heights[i], heights[j])
            b = j - i
            mx = max(l*b, mx)
            if (heights[i]<=heights[j]):
                i+=1
            else:
                j-=1
        
        return mx