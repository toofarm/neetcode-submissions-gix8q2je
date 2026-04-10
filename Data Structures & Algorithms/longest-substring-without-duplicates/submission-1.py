import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left = 0
        right = 0
        longest = 0
        seen = collections.defaultdict(int)

        while right < len(s):
            seen[s[right]] += 1
            right += 1

            if max(seen.values()) == 1:
                longest = max(right - left, longest)
            else:
                seen[s[left]] -= 1
                left += 1

        return longest


        