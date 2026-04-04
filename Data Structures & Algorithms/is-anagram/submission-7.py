class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): return False
        mp1 = {}
        mp2 = {}
        for i in range(len(s)):
            if s[i] in mp1.keys():
                mp1[s[i]] += 1
            else:
                mp1[s[i]] = 1
            
            if t[i] in mp2.keys():
                mp2[t[i]] += 1
            else:
                mp2[t[i]] = 1
        
        for key in mp1.keys():
            if mp1[key] != mp2.get(key):
                return False
        return True 

