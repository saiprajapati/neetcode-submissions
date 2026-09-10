import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^a-zA-Z0-9]', '', s)
        st = text.lower()
        return st == st[::-1]