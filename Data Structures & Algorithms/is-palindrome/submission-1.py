class Solution:
    def isPalindrome(self, s: str) -> bool:
        def skip_simbol(s, i, step):
            while s[i] in {" ", ",", ".", "?", '\''} and 0 <= i < len(s):
                i += step
            return i

        i, j = 0, len(s) - 1

        while i < j:
            i = skip_simbol(s, i, +1)
            j = skip_simbol(s, j, -1)

            if s[i].lower() != s[j].lower():
                break
            i += 1
            j -= 1

        return i >= j