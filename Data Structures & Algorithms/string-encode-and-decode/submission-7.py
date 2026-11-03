class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += f'{len(word)}#{word}'
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        res = []
        while i < len(s):
            tag_index = s.find("#", i)
            word_len = int(s[i:tag_index])
            i = tag_index + word_len + 1
            res.append(s[tag_index + 1:i])
        return res
