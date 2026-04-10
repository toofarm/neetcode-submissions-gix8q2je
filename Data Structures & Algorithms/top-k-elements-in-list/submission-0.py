class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums

        memo = { }

        for num in nums:
            if num not in memo:
                memo[num] = 0
            memo[num] += 1

        res = []

        sortedMemo = { key: value for key, value in sorted(memo.items(), 
            key=lambda item: item[1], reverse=True)}

        for key, val in sortedMemo.items():
            res.append(key)

        return res[:k]
