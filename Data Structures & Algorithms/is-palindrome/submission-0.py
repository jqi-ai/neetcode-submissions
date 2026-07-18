class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        start, end = 0, len(s) - 1
        while start < end:
            while start < len(s) and s[start].isalnum() == False:
                start += 1
            while end > -1 and s[end].isalnum() == False:
                end -= 1
            if start < end and s[start].isalnum() and s[end].isalnum() and s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            elif start >= end:
                break
            else:
                return False
        return True