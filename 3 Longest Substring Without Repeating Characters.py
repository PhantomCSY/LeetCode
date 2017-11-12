# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


    def lengthOfLongestSubstring(self, s):
        max_len = 0
        i = 0
        char = {}
        
        for j in range(len(s)):
            if i <= char.get(s[j], 0):
                i = char.get(s[j], -1) + 1
            char[s[j]] = j
            temp = j - i + 1
            
            if temp > max_len:
                max_len = temp
                
        return max_len
