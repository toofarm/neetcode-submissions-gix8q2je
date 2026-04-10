class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        s = set(nums)
        res = 0
        curr = 1

        for num in s:
            if num - 1 not in s and num + 1 in s:
                flag = True
                curr_num = num

                while flag:
                    if curr_num + 1 in s:
                        curr += 1
                        curr_num = curr_num + 1
                    else:
                        flag = False

            prev_num = num
            res = max(res, curr)
            curr = 1

        return res
        