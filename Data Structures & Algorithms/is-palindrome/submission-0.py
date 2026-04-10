import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        s = re.sub(r"\W", "", s).lower()

        left = len(s) // 2 - 1

        if len(s) % 2 == 0:
            right = len(s) // 2
        else:
            right = len(s) // 2 + 1

        while left >= 0 and right <= len(s) - 1:
            if s[left] != s[right]:
                return False

            left -= 1
            right += 1

        return True