import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_vals = [0 for i in range(26)]
        s2_vals = [0 for i in range(26)]

        for c in s1:
            s1_vals[ord(c) - 97] += 1
            
        left = 0
        right = 0

        while right < len(s2):
            s2_vals[ord(s2[right]) - 97] += 1
            right += 1

            if s1_vals == s2_vals:
                return True
            
            if right - left == len(s1):
                s2_vals[ord(s2[left]) - 97] -= 1
                left += 1

        return False
