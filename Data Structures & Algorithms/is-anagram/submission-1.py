class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = {}

       
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        
        for char in t:
            if char not in hashmap:
                return False

            hashmap[char] -= 1

            if hashmap[char] < 0:
                return False

        for value in hashmap.values():
            if value != 0:
                return False

        return True