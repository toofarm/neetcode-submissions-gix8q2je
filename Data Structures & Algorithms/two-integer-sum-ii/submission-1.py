class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def do_binary(nums: List[int], target: int, initial: int):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2
                s = nums[mid] + nums[initial]

                if s == target:
                    return sorted([initial + 1, mid + 1])
                elif s > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return False

        for i in range(len(numbers)):
            res = do_binary(numbers, target, i)
            if res is not False:
                return res