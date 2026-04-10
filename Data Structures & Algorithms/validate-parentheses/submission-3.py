class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in pairs.keys():
                if len(stack) and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0