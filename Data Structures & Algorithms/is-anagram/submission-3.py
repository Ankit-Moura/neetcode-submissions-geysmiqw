class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): return False
        lst = list(t)
        for letter in s:
            if not letter in lst:
                return False
            lst.remove(letter)
        return True