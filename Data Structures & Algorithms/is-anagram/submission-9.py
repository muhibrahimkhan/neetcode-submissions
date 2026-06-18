class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for key in s:
            if key in dict_s:
                dict_s[key] += 1
            else:
                dict_s[key] = 1
        
        for key in t:
            if key in dict_t:
                dict_t[key] += 1
            else:
                dict_t[key] = 1
        
        return dict_s == dict_t
