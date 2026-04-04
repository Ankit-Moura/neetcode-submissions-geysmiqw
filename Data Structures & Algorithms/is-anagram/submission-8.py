class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst = [0]*26
        if len(s)!= len(t): return False
        for x in range(len(s)):
            i =  ord(s[x]) - ord('a') 
            j =  ord(t[x]) - ord('a') 
            lst[i] += 1
            lst[j] -= 1
        
        return all(x == 0 for x in lst)

