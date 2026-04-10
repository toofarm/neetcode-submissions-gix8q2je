import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        max_len = 0
        right = 0
        left = 0
        counts = collections.defaultdict(int)

        while right < len(s):
            counts[s[right]] += 1
            right += 1

            max_freq = max(counts.values()) if counts else 0
            window_length = len(s[left:right])

            if window_length - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            else:
                max_len = max(window_length, max_len)

        return max_len
            

