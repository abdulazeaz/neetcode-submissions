class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            freqs = [0] * 26
            for char in word:
                freqs[ord(char) - 97] += 1
                        
            key = "|".join(map(str, freqs))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())
