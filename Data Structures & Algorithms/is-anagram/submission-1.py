class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_ = [0] * 26

        for i in range(len(s)):
            map_[ord(s[i]) - ord('a')] += 1
            map_[ord(t[i]) - ord('a')] -= 1
        
        for i in map_:
            if i != 0:
                return False
        return True