class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        memo = { }
        res = [ ]

        for s in strs:
            canon = ''.join(sorted(s))

            if canon not in memo:
                memo[canon] = []

            memo[canon].append(s)

        for val in memo.values():
            res.append(val)

        return res
