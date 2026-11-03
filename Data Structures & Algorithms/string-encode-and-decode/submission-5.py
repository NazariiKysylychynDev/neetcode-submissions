class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        counter = ''
        for word in strs:
            res = res + word
            counter = str(len(word)) + counter
        return res + counter

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, len(s) - 1

        while i < j:
            index = int(s[j])
            res.append(s[i:i+index])

            j -= 1
            i += index
        return res