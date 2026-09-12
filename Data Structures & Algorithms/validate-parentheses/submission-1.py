class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in d.keys():
                stack.append(d[i])
            else:
                if not stack:
                    return False
                if i == stack[-1]:
                    stack.pop()
                    continue
                else: 
                    return False
        if stack:
            return False
        return True