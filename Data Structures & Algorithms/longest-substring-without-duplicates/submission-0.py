class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        set_ = set()

        left = 0
        for right in s:
            while right in set_:
                set_.remove(s[left])
                left += 1

            set_.add(right)
            
            max_ = max(len(set_), max_)
        
        return max_