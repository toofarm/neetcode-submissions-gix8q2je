class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mem = { }

        for i in range(len(s)):
            if s[i] in mem:
                mem[s[i]] += 1
            else:
                mem[s[i]] = 1

            if t[i] in mem:
                mem[t[i]] -= 1
            else:
                mem[t[i]] = -1

        for key in mem:
            if mem[key] != 0:
                return False

        return True