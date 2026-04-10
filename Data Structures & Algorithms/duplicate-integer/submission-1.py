class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False