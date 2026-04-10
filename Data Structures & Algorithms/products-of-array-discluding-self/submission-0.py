class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        right_product = 1
        j = len(nums) - 1

        while j >= 0:
            res[j] *= right_product
            right_product *= nums[j]
            j -= 1

        return res


