class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        treasure = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == -nums[i] and [nums[i], nums[left], nums[right]] not in treasure:
                    treasure.append([nums[i], nums[left], nums[right]])
                elif s < -nums[i]:
                    left += 1
                else:
                    right -= 1

        return treasure
                