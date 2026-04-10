class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        s = sorted(set(nums))
        print(s)
        res = 0
        curr = 0
        prev_num = None

        for num in s:
            if prev_num is None:
                curr += 1
            elif prev_num + 1 == num:
                curr += 1
            else:
                curr = 1

            prev_num = num
            res = max(res, curr)

        return res
        