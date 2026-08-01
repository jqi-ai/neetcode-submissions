class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{' : '}', '[': ']'}
        for ch in s:
            if ch in mapping.keys():
                stack.append(ch)
            elif ch in mapping.values():
                if not stack:
                    return False
                paired = stack.pop()
                if mapping[paired] != ch:
                    return False
            else:
                continue
        return True