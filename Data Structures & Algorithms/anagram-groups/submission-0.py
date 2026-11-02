class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map_ = dict()
        res = []
        
        for case in strs:
            sorted_case = str(sorted(case))
            
            if sorted_case in map_:
                res[map_[sorted_case]].append(case)
            else:
                res.append([case])
                map_[sorted_case] = len(res) - 1
        return res