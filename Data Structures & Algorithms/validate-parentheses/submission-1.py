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
                if len(stack) and stack[len(stack) - 1] == pairs[char]:
                    stack.pop(len(stack) - 1)
                else:
                    return False
            else:
                stack.append(char)

        return True if len(stack) == 0 else False