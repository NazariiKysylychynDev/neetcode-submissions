class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = left = 0
        set_ = dict()

        for i, right in enumerate(s):            
            if right in set_:
                left = max(set_[right] + 1, left)

            set_[right] = i
            # set_.add(right)
            max_ = max(max_, i - left + 1)
        
        return max_
