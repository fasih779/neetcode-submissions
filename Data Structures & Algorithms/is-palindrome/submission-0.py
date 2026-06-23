class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        e = ""

        for ch in s:
            if ch.isalnum():
                e += ch.lower()

        
        for i in range(len(e)):
            if e[i] != e[len(e) - 1 - i]:
                return False
     
        return True
        print(e)    