class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for letter in s:
            if letter.isalnum():
                lst.append(letter.lower())

        
        st = 0
        end = len(lst)-1

        while(st<=end):
            if lst[st]!=lst[end]:
                return False
            st+=1
            end-=1
        
        return True
            

        