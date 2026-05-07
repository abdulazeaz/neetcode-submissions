class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        
        for char in t:
            if char not in letters or letters[char] == 0:
                return False
            letters[char] -= 1
        
        return True