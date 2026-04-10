class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        memo = { }
        longest = 1
        left = 0
        right = 0

        while right < len(s):
            if s[right] in memo:
                while s[right] in memo:
                    memo.pop(s[left])
                    left += 1
            else:
                longest = max((right - left) + 1, longest)

            memo[s[right]] = True
            right += 1

        return longest


