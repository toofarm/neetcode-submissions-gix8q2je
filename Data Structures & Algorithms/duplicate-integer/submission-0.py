class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        mem = { }

        for i in range(len(nums)):
            if nums[i] in mem:
                return True
            else:
                mem[nums[i]] = True

        return False