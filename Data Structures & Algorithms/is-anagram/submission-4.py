class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}

        for char in s:
            if char not in m:
                m[char] = 1
            else:
                m[char] += 1
        
        for char in t:
            if char not in m:
                return False
            
            if m[char] <= 0:
                return False
            
            m[char] -= 1
        
        for k, v in m.items():
            if v != 0:
                return False

        return True