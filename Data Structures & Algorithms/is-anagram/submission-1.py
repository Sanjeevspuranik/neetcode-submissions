class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_dict = {}

        for i in range(len(s)):
            char_dict[s[i]] = char_dict.get(s[i], 0) + 1
            char_dict[t[i]] = char_dict.get(t[i], 0) - 1
        
        for count in char_dict.values():
            if count != 0:
                return False
        
        return True