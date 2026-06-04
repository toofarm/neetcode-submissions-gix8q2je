class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            # print(f"low: {low}")
            # print(f"high: {high}")
            # print(f"low + (high - low): {low + (high - low)}")
            # print(f"{low + (high - low)} // 2: {low + (high - low) // 2}")
            # print(f"mid: {mid}")
            # print('*************')

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1