class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        memo = { }

        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [memo[target - nums[i]], i]

            memo[nums[i]] = i
