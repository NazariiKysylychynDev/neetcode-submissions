class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {"[": "]", "(": ")", "{": "}"}
        stack=[]
        
        for i in s:
            if i in map_.keys():
                stack.append(i)
            elif i in map_.values():
                if stack and map_[stack[-1]] == i:
                    stack.pop()
                else:
                    break
        return not stack
